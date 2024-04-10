#! /bin/python3

import requests
import sys
import os

def getGSheet(sheet_id, output_file):
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, 'wb') as fp:
            fp.write(response.content)
            print("Data successfully saved.")
    else:
        print(f'Unable to download Google Sheet: {response.status_code}')
        sys.exit(1)


sheet_id = "1PrtZeMkV6yJmlWq2jYiTVNqBUCV8JBBFHouClqXg6vU"
output_file = "data.csv"

getGSheet(sheet_id, output_file)
sys.exit(0)
