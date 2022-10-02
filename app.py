from crypt import methods
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')   

@app.route('/results', methods=['POST'])
def render_results():
    
    city_name = request.form['city_name']
    my_api_key = '974b6905630d60c93952b5f4679b3da1'
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+my_api_key)

    #read the json object
    json_object = r.json()

    #get the attributes
    temperature = str(int(json_object['main']['temp']-273.15)) #converts from kelvin    
    condition = str(json_object['weather'][0]['main']        )
    
    return 'Currently, the weather in '+city_name+' is '+temperature+' degrees and the sky is '+condition

#app.run(host='0.0.0.0', port=81, debug=True, use_reloader=True)

if __name__ == "main":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

