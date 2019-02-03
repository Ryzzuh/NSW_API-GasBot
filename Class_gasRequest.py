#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:10:30 2018

@author: rhysall
"""

import requests
import json
import base64
import get_secret.ecodeSecretKey as secret_key

class gasRequest():

    def init(self):
        pass
    
    # for instruction see https://api.nsw.gov.au/How-Tos
    def getOauthKey(self, keySecret):
        url = 'https://api.onegov.nsw.gov.au/oauth/client_credential/accesstoken'\
                '?grant_type=client_credentials'
        headers = {'Authorization': 'Basic {}'.format(keySecret)\
                   ,'dataType': 'json'}
        r = requests.get(url, headers=headers)
        json_data = json.loads(r.text)
        return json_data['access_token']
        
    
    def getFuelPrices(self, oauthKey):
        #will need to collect new auth each time, see docs
        headers = {
                    'apikey': 'J5BpUAfdF2ivg1IXOASqkG2pQTHoO9FW'\
                   , 'transactionid': 'qadec'\
                   ,'requesttimestamp': '14/01/2018 15:41:30'\
                   ,'Content-Type': 'application/json; charset=utf-8'\
                   ,'Authorization': 'Bearer {}'.format(oauthKey) \
                   }
        url = 'https://api.onegov.nsw.gov.au/FuelPriceCheck/v1/fuel/prices'
        r = requests.get(url, headers=headers)
        return r.text
        
rq = gasRequest()
rq.secretKey = rq.encodeSecretKey()
rq.Oauth = rq.getOauthKey(rq.secretKey)
fuelPrices = rq.getFuelPrices(rq.Oauth)
print(fuelPrices)
