from flask import Flask, request
from kwikSystemDatabaseUpload import kwicSystemDatabaseUpload
import Constants

app = Flask(__name__)

@app.route('/', methods=['GET',])
def runKwicWebserver():
	originalUrlKeywords = request.args.get(Constants.GET_ARG_ORIGINAL_URL_KEYWORDS)

	noiseWords = request.args.get(Constants.GET_ARG_NOISE_WORDS)

	return kwicSystemDatabaseUpload(originalUrlKeywords, noiseWords)