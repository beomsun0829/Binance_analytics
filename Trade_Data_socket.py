import csv
import json

import os
import time

def Trade_Data_socket(rawdata):
    
    with open("Trade_Data" + '.csv', 'a', newline='') as csv_file:
        
        writer = csv.writer(csv_file)
        JSON_DATA = json.loads(rawdata)
        
        #parse the json data (only ORDER_TRADE_UPDATE)
        if JSON_DATA['e'] == "ORDER_TRADE_UPDATE":
            ORDER_TRADE_UPDATE_DATA = JSON_DATA['o']
            
            writer.writerow([
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ORDER_TRADE_UPDATE_DATA['T']/1000)),
                ORDER_TRADE_UPDATE_DATA['s'],
                ORDER_TRADE_UPDATE_DATA['S'],
                ORDER_TRADE_UPDATE_DATA['o'],
                ORDER_TRADE_UPDATE_DATA['q'],
                ORDER_TRADE_UPDATE_DATA['p'],
                ORDER_TRADE_UPDATE_DATA['x'],
                ORDER_TRADE_UPDATE_DATA['X'],
                ORDER_TRADE_UPDATE_DATA['wt'],
                ORDER_TRADE_UPDATE_DATA['ot'],
                ORDER_TRADE_UPDATE_DATA['ps']
                ])
            
            
def check_csv_exists():
    #if csv file not exist, create it
    if not os.path.exists('Trade_Data.csv'):
        with open('Trade_Data.csv', 'w', newline='') as csv_file:
            fieldnames = [
                'Time',
                'Symbol',
                'Side',
                'Order Type',
                'Original Quantity',
                'Original Price',
                'Execution Type',
                'Order Status',
                'Stop Price Working Type',
                'Original Order Type',
                'Position Side'
                ]
            
            
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()