import Constants
import requests

class DatabaseController:

	def __init__(self):
		pass

	def upload(self, originalUrlKeywords, kwicUrlKeywords, noiseWords):

		success = True
		error = None
		try:
			#Recieve a response from the Server
			response = requests.get(Constants.DATABASE_URL, params={Constants.GET_ARG_NOISE_WORDS: noiseWords, Constants.GET_ARG_ORIGINAL_URL_KEYWORDS: originalUrlKeywords, Constants.GET_ARG_KWIC_URL_KEYWORDS: kwicUrlKeywords, Constants.GET_ARG_REQUEST_TYPE: Constants.REQUEST_TYPE_UPLOAD}, timeout = 60)
			if response.text == Constants.SERVER_RESPONSE_UPLOAD_FAILURE:
				raise Exception(Constants.SERVER_RESPONSE_UPLOAD_FAILURE)

		except Exception as e:
			success = False
			error = e
		finally:
			if not success:
				raise error




	def getQueryResults(self, keywords):
		queryResults = ""
		success = True
		error = None
		try:	
			queryResults = requests.get(Constants.DATABASE_URL, params={Constants.GET_ARG_KEYWORDS: keywords, Constants.GET_ARG_REQUEST_TYPE: Constants.REQUEST_TYPE_QUERY}, timeout=60)
			if queryResults == Constants.SERVER_RESPONSE_QUERY_FAILURE:
				raise Exception('SEARCH FAILURE')

		except Exception as e:
			error = e
			success = False
		finally:
			if success:
				return queryResults
			else:
				raise error
