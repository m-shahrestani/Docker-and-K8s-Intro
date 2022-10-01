import requests
import os
import flask
import socket
import json


resdict = {
            "port" : 8080,
            "URL": "http://api.weatherstack.com/current?access_key=304d4910bc112ec2cbed8d8073dbcaea&query=Tehran"
            }
if os.path.exists('conf.json'):
    file = open('conf.json')
    resdict = json.load(file)



if __name__=='__main__':
    app = flask.Flask('p2')
    @app.route('/api')
    def apifunc():
        response = requests.get(resdict['URL']).json().get('current')
        return {'temperature' : response.get('temperature'),
                'weather_descriptions' : response.get('weather_descriptions'),
                'wind_speed' : response.get('wind_speed'),
                'humidity' : response.get('humidity'),
                'feelslike' : response.get('feelslike'),
                'hostname' : socket.gethostname()
        }
    app.run('0.0.0.0', resdict['port'])

