import socket
import Constants

class DatabaseController:

	def __init__(self):
		pass

	def upload(self, originalUrlKeywords, kwicUrlKeywords, noiseWords):

		success = True
		error = None
		try:
			SERVER_IP = 'localhost'  
			PORT = 12001

			#Create Client Socket
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			print('created')
			client_socket.settimeout(10)

			#Connect to Server Socket
			client_socket.connect((SERVER_IP, PORT))
			client_socket.settimeout(10)

			#Send Message to Server
			client_socket.sendall(Constants.REQUEST_TYPE_UPLOAD)
			response = client_socket.recv(100)
			if response == Constants.SERVER_RESPONSE_UPLOAD_FAILURE:
				raise Exception(Constants.SERVER_RESPONSE_UPLOAD_FAILURE)

			client_socket.sendall(originalUrlKeywords.encode('utf-8'))
			response = client_socket.recv(100)
			if response == Constants.SERVER_RESPONSE_UPLOAD_FAILURE:
				raise Exception(Constants.SERVER_RESPONSE_UPLOAD_FAILURE)
			client_socket.sendall(kwicUrlKeywords.encode('utf-8'))

			response = client_socket.recv(100)
			if response == Constants.SERVER_RESPONSE_UPLOAD_FAILURE:
				raise Exception(Constants.SERVER_RESPONSE_UPLOAD_FAILURE)
			client_socket.sendall(noiseWords.encode('utf-8'))

			#Recieve a response from the Server
			client_socket.settimeout(60)
			response = client_socket.recv(100)
			print('Received:', response.decode('utf-8'))
			if response == Constants.SERVER_RESPONSE_UPLOAD_FAILURE:
				raise Exception(Constants.SERVER_RESPONSE_UPLOAD_FAILURE)

		except Exception as e:
			success = False
			error = e
		finally:
			client_socket.close()
			if not success:
				raise error




	def getQueryResults(self, keywords):
		queryResults = ""
		success = True
		error = None
		try:


			keywords = keywords.encode('utf-8')


			SERVER_IP = 'localhost'  
			PORT = 12001

			#Create Client Socket
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			print('created')
			client_socket.settimeout(10)

			#Connect to Server Socket
			client_socket.connect((SERVER_IP, PORT))
			client_socket.settimeout(10)

			#Send Message to Server
			client_socket.sendall(Constants.REQUEST_TYPE_QUERY)
			queryResults = client_socket.recv(100)
			client_socket.sendall(keywords)

			#Recieve a response from the Server
			client_socket.settimeout(120)
			queryResults = client_socket.recv(500000)
			print('Received:')
			if queryResults == Constants.SERVER_RESPONSE_QUERY_FAILURE:
				raise Exception('SEARCH FAILURE')

		except Exception as e:
			error = e
			success = False
			print(e)
		finally:

			client_socket.close()

			if success:
				return queryResults
			else:
				raise error
