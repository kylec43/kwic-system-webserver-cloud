from flask import Flask, request
from kwikSystemDatabaseUpload import kwicSystemDatabaseUpload
import Constants

app = Flask(__name__)

@app.route('/', methods=['GET',])
def runKwicWebserver():
	originalUrlKeywords = request.args.get(Constants.GET_ARG_ORIGINAL_URL_KEYWORDS)
	originalUrlKeywords = originalUrlKeywords.text

	noiseWords = request.args.get(Constants.GET_ARG_NOISE_WORDS)
	noiseWords = noiseWords.text

	return kwicSystemDatabaseUpload(originalUrlKeywords, noiseWords)