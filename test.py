from flask import Flask, request
import requests
import Constants

url = Constants.DATABASE_URL

r = requests.get('https://kwic-project.uc.r.appspot.com', params={'data': 'echo this'})
print(r.text)