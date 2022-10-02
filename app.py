#Code created by Gabriel Oliveira 
#for AIDI 1001: Conversational AI - Week 4 Task

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
    #Creates a responde and sends it back to Dialogflow
    return make_response(jsonify(send_results())) 

def send_results(): 
    #Build a request object 
	req = request.get_json(force=True) 

	#Fetch city name from Dialogflow
    city_name = req.get('queryResult').get('geo-city')
    my_api_key = '974b6905630d60c93952b5f4679b3da1'
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+my_api_key)
    
    #Read the response from Weather API and parse the attributes
    json_object = r.json()
    temperature = str(int(json_object['main']['temp']-273.15)) #converts from kelvin    
    condition = str(json_object['weather'][0]['main'])

	#Returns the response 
	speech = "Currently, temperature in " + city_name + " is " + temperature + " and the sky is/has " + condition
    
    return {
        "speech": speech,
        "displayText": speech,
    }

if __name__ == "main":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

    #app.run(
    # debug=True, 
    # use_reloader=True,
    # host='0.0.0.0', 
    # port=int(os.environ.get("PORT", 5000))
    #)


