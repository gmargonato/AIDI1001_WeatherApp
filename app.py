from crypt import methods
from flask import Flask, render_template, request, make_response, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/') 
def index(): 
	return 'Hello :)'

@app.route('/webhook', methods=['GET', 'POST']) 
def webhook(): 
	# return response for webhooks
	return make_response(jsonify(send_results())) 

def send_results(): 
	# build a request object 
	req = request.get_json(force=True) 

	# fetch action from json 
	action = req.get('queryResult').get('geo-city') 

	# return a fulfillment response 
	return {'fulfillmentText': 'This is a response from webhook.'} 

#app.run(
# host='0.0.0.0', 
# port=int(os.environ.get("PORT", 5000)), 
# debug=True, 
# use_reloader=True
#)

if __name__ == "main":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

