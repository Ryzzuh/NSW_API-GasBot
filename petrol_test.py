#!flask/bin/python3.6
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:40:44 2018

@author: rhysall
"""
#!flask/bin/python3.6
from flask import Flask
from flask import url_for
from flask import jsonify
import requests
import json
import base64
import pprint 
pp = pprint.PrettyPrinter(indent=4)
import get_secret.ecodeSecretKey as secret_key
app = Flask(__name__)

@app.route('/')
def index():

    
    # for instruction see https://api.nsw.gov.au/How-Tos
    def getOauthKey(keySecret):
        url = 'https://api.onegov.nsw.gov.au/oauth/client_credential/accesstoken'\
                '?grant_type=client_credentials'
        headers = {'Authorization': 'Basic {}'.format(keySecret)\
                   ,'dataType': 'json'}
        r = requests.get(url, headers=headers)
        print(r.text)
        json_data = json.loads(r.text)
        print(json_data['access_token'])
        return json_data['access_token']
        
    
    def getFuelPrices(oauthKey):
        #will need to collect new auth each time, see docs
        headers = {'apikey': 'J5BpUAfdF2ivg1IXOASqkG2pQTHoO9FW', 'transactionid': 'qadec', 'requesttimestamp': '14/01/2018 15:41:30', 'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer {}'.format(oauthKey)}
        url = 'https://api.onegov.nsw.gov.au/FuelPriceCheck/v1/fuel/prices'
        r = requests.get(url, headers=headers)
        print(r.text)
        return jsonify(r.json())
        #return r.text
    
    #return getFuelPrices(getOauthKey(encodeSecretKey()))
    return url_for('<int:station_id>')

@app.route('/<int:station_id>')
def profile(station_id):
    return jsonify(station_id)

if __name__ == '__main__':

    app.run(debug=True)