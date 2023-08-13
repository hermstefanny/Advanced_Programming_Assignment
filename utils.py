#Packet importing
import os
import csv
import json
import pandas as pd

#functions definition


def check_file_format(filename):
    
    if os.path.splitext(filename)[1].lower() == '.csv':
        print('File is CSV')
        return 'CSV'

    elif os.path.splitext(filename)[1].lower() == '.json':
        print('File is JSON')
        return 'JSON'
      
    else:
        print('Unknown file extension')
        return ''

def load_file(filename):
    file = open(filename, 'r', encoding='latin-1')
    return file






