from LineManager import LineManager
from CircularShift import CircularShift
from Alphabetizer import Alphabetizer
import re
import time
import Constants
import socket
from DatabaseController import DatabaseController

def kwicSystemDatabaseUpload(originalUrlKeywords, noiseWords):

	success = True
	databaseController = DatabaseController()
	try:
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
		circularShift = CircularShift(lineManager, noiseWordsList)
		alphabetizer = Alphabetizer(lineManager, circularShift.getOffsets())

		sortedOffsets = alphabetizer.GetSortedOffsets()

		kwicUrlKeywordsFormatted = formatDatabaseOutputString(urls, lineManager, sortedOffsets)
		noiseWords = formatDatabaseNoiseWords(noiseWords)

		success = True

		databaseController.upload(originalUrlKeywords, kwicUrlKeywordsFormatted, noiseWords)


	except Exception:
		success = False

	finally:
		# Close the client connection after the try or except block
		if success:
			return Constants.SERVER_RESPONSE_UPLOAD_SUCCESS
		else:
			return Constants.SERVER_RESPONSE_UPLOAD_FAILURE



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
	




