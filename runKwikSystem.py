from LineManager import LineManager
from CircularShift import CircularShift
from Alphabetizer import Alphabetizer
import re
import time
import Constants
import socket
from DatabaseController import DatabaseController

def runKwicSystem(parent, connection, client_address):

	success = True
	databaseController = DatabaseController()
	try:
		buffer_size = 500000
		#Recieve input lines and noise words from client.
		connection.settimeout(10)
		originalUrlKeywords = connection.recv(buffer_size)
		connection.sendall(b'received')
		noiseWords = connection.recv(buffer_size)

		#convert data to string!
		originalUrlKeywords = originalUrlKeywords.decode('utf-8')
		noiseWords = noiseWords.decode('utf-8')

		print("Recieved data from client:", client_address)


		total_time_start = time.time()

		#get URL and Keywords
		UrlAndKeywords = getUrlAndKeywords(originalUrlKeywords)
		keywords = []
		urls = []
		for i in range (len(UrlAndKeywords)):
			urls.append(UrlAndKeywords[i][0])
			keywords.append(UrlAndKeywords[i][1])

		#get noiseWords
		noiseWordsList = getNoiseWords(noiseWords)



		lineManager = LineManager(keywords)


		time_start = time.time()
		circularShift = CircularShift(lineManager, noiseWordsList)
		time_end = time.time()
		total_time = time_end-time_start
		print("circular shift", total_time)

		time_start = time.time()
		print('offsets', len(circularShift.getOffsets()))
		alphabetizer = Alphabetizer(lineManager, circularShift.getOffsets())
		time_end = time.time()
		total_time = time_end-time_start
		print("alphabetizer", total_time)

		sortedOffsets = alphabetizer.GetSortedOffsets()

		time_start = time.time()
		kwicUrlKeywordsFormatted = formatDatabaseOutputString(urls, lineManager, sortedOffsets)
		noiseWords = formatDatabaseNoiseWords(noiseWords)

		success = True
		try:
			databaseController.upload(originalUrlKeywords, kwicUrlKeywordsFormatted, noiseWords)
		except Exception as e:
			raise e

		time_end = time.time()
		total_time = time_end-time_start
		print('output', total_time)

		total_time_end = time.time()
		total_time = total_time_end - total_time_start
		print('total time', total_time)
		print('---------------------------------------------------')

	except Exception as e:
		success = False
		print("Error has occured:", e)

	finally:
		# Close the client connection after the try or except block
		if success:
			connection.sendall(Constants.SERVER_RESPONSE_UPLOAD_SUCCESS)
		else:
			print('failed')
			connection.sendall(Constants.SERVER_RESPONSE_UPLOAD_FAILURE)

		connection.close()
		print("Connection has been closed")



def getUrlAndKeywords(string):
	UrlAndKeywords = []
	inputLines = string.split('\n')
	print(inputLines)
	for i in range(len(inputLines)):
		inputLines[i] = inputLines[i].split()
		url = inputLines[i][0]
		keywords = " ".join(inputLines[i][1:])
		UrlAndKeywords.append((url, keywords))

	return UrlAndKeywords

def getNoiseWords(noiseWords):
	return noiseWords.split()



def formatDatabaseOutputString(urls, lineManager, offsets):
	formattedData = ''
	for i in range(len(offsets)):
		formattedData += (urls[offsets[i][0]] + ' ' + lineManager.getOffsetLine(offsets[i][0], offsets[i][1]) + '\n')

	return formattedData


def formatDatabaseNoiseWords(noiseWords):
	return " ".join(getNoiseWords(noiseWords))
	




