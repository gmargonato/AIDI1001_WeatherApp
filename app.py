#Code created by Gabriel Oliveira 
#for AIDI 1001: Conversational AI - Week 4 Task

from crypt import methods
from flask import Flask, render_template, request, make_response, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/') 
def index():
    #Deprecated
    #return render_template('index.html')   
    return jsonify(
        student_name = 'Gabriel Oliveira',
        student_id   = '200499674'
    )

@app.route('/webhook', methods=['POST']) 
def webhook(): 

    #Information received from Dialogflow
    req = request.get_json(force=True) 
    query_result = req.get('queryResult')

    #Get the city name
    city_name = query_result.get('parameters').get('geo-city')
    
    #Make the request to Open Weather Map API
    my_api_key = '974b6905630d60c93952b5f4679b3da1'
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+my_api_key)
    
    #Read the response and parse the attributes
    json_object = r.json()
    temperature = str(int(json_object['main']['temp']-273.15)) #converts from kelvin    
    condition = str(json_object['weather'][0]['main'])

	#Returns the response 
    message = "Currently, temperature in " + city_name + " is " + temperature + " degress Celcius and the sky is/has " + condition
    
    return {
        "fulfillmentText": message,
        "source": 'webhook'
    }

test_mode = 0
port = int(os.environ.get("PORT", 5000))

if __name__ == "main":
    if test_mode == 0:
        app.run(debug=False, host='0.0.0.0', port=port)
    else:
        app.run(debug=True, use_reloader=True, host='0.0.0.0', port=port)
