#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:10:30 2018

@author: rhysall
"""


import requests
import json
import base64
import pandas as pd
import os
import get_secret.ecodeSecretKey as secret_key

dir_path = os.path.dirname(os.path.realpath(__file__))
print(os.getcwd())


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
    #print(r.text)
    #print(r.headers)
    json = r.json()
    print("json ",json)
    return json
    #[d['stationcode'] for d in list if d['fueltype'] == "U91"]

def to_pandas_dataframe(price_list):
    df = pd.DataFrame(price_list)
    df.to_csv('outputs/1234.csv')
    
def to_txt(price_list):
    #print(price_list)
    with open("outputs/Output.json", "w") as outfile:
        json.dump(price_list, outfile)
    
print("starting")
price_list = getFuelPrices(getOauthKey(secret_key))
to_txt(price_list)
print(encodeSecretKey())
#to_pandas_dataframe(price_list)
#getFuelPrices("v3G5lILzIn4iORqQnp7no7VGnpsA")