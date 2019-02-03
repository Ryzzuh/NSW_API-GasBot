#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:10:30 2018

@author: rhysall
"""
'''
for postcode regions see...
https://www.training.nsw.gov.au/about_us/postcodes_byregion.html
'''

import json
import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
#print(os.getcwd())

 


def to_pandas_dataframe(key):
    with open('outputs/Output.json', 'r') as f:
        data = json.load(f)
        prices = data[key]
    df = pd.DataFrame(prices)
    return df

df_prices = to_pandas_dataframe('prices')
#print(df_prices.head())
print(df_prices.describe().iloc['mean'])

df_stations = to_pandas_dataframe('stations')
#print(df_stations.head())


