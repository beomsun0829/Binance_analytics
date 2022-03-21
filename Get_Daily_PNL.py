import csv
import json

import os
import time
import config

import ccxt


def Get_Daily_PNL():
    
    print ("CCXT VERSION : " + ccxt.__version__)
    exchange = ccxt.binance({
        'apiKey': config.API_CONFIG["APIKEY"],
        'secret': config.API_CONFIG["SECRETKEY"],
        'enableRateLimit': True, # required https://github.com/ccxt/ccxt/wiki/Manual#rate-limit
        'options': {
            'defaultType': 'future',
        },
    })
    response = exchange.fetch_balance()
    print(response['total']['USDT'], response['total']['BUSD'])
    
    with open("Daily_PNL" + '.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow([
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
            response['total']['USDT'],
            response['total']['BUSD']
            ])
