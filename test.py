from flask import Flask, request
import requests

url = 'https://kwic-project.uc.r.appspot.com'

r = requests.get(url, params={'data': 'echo this'})
print(r.text)