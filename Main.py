import time
import logging
import json
import os
import sys
import traceback
from colorama.ansi import Back, Fore, Style
from Utility import Utility
import csv
import requests

class Main:

    def __init__(self):      
        self.util = Utility()
        self.log_count = 0
        self.fname = "fraud-dataset"
        self.fpath = "../data/"
        self.rpath = "../resources/"

    def log_progress(self, msg):
        print(f'{msg}', end='\r')

    def split_dataset(self, start):

        start_ts = self.util.get_ts(start)
        now = start_ts
        data = {}

        with open(f"{self.rpath}{self.fname}.csv", "r") as f:
            csvReader = csv.DictReader(f)
            s1 = 1
            hours = 0
            day = 1
            for r in csvReader:
                # for each day, write a json file to split the dataset 
                s0 = int(r['step'])
                if s1 != s0: 
                    if s0 % 24 == 0: day += 1
                    fday = f"{self.fpath}{self.fname}_{start_ts+((day-1)*24*3600)}.json"
                    s1 = s0
                    self.util.write_json(data, fday)
                    data = {}
                    now = start_ts + (s1*3600)
                    self.log_progress( f"Processing: {self.util.get_iso_datetime(now)}" )

                now = now + 1
                key = f"{self.util.current_milis()}_{r['nameOrig']}"
                obj = { 
                    "type": r["type"], "amount": float(r["amount"]) , "nameOrig": r["nameOrig"] ,
                    "oldbalanceOrg": float(r["oldbalanceOrg"]) , "newbalanceOrig": float(r["newbalanceOrig"]),
                    "nameDest": r["nameDest"], "oldbalanceDest": float(r["oldbalanceDest"] ), 
                    "newbalanceDest": float(r["newbalanceDest"]), "isFraud": int(r["isFraud"]), "isFlaggedFraud": int(r["isFlaggedFraud"]),
                    "datetime": self.util.get_iso_datetime_sec(now)
                }

                data[key] = obj

    def upload(self, start, end):
        start_ts = self.util.get_ts(start)
        end_ts = self.util.get_ts(end)
        day = start_ts
        print(day, start_ts, end_ts)
        while day <= end_ts:
            self.log_progress(f"processing day={self.util.get_iso_datetime(day)}")
            fday = f"{self.fpath}{self.fname}_{day}.json"
            data = self.util.read_json(fday)
            self.util.bulk_create("fraud-dataset", data )
            day = day + 24*3600

    def _get_action(self, o):
        actions = {"TRANSFER": "transfer", "DEBIT": "debit", "CASH_IN": "cashin", "CASH_OUT": "cashout", "PAYMENT": "payment"}
        return actions[o['type']]

    def simulation(self, start, end):
        start_ts = self.util.get_ts(start)
        end_ts = self.util.get_ts(end)
        day = start_ts
        print(day, start_ts, end_ts)
        while day <= end_ts:
            self.log_progress(f"processing day={self.util.get_iso_datetime(day)}")
            fday = f"{self.fpath}{self.fname}_{day}.json"
            data = self.util.read_json(fday)
            t = time.time()
            for k in data:
                o = data[k]
                t = time.time()
                headers = {'Content-Type': 'application/json'}
                action = self._get_action(o)
                r = requests.post(f'http://127.0.0.1:5000/bank/{action}', json = o, headers=headers )
            day = day + 24*3600



#######################
#
#######################

def main(argv):

    if len(argv) < 2:
        print(f'{Fore.YELLOW}usages:{Style.RESET_ALL}')
        print('   python3 Main.py SplitDataset yyyymmdd')
        print('   python3 Main.py Upload yyyymmdd yyyymmdd')
        return 
    
    m = Main()
    if argv[0] == "SplitDataset":
        start = argv[1] 
        m.split_dataset(start)
    elif argv[0] == "Upload":
        start = argv[1]
        end = argv[2]
        m.upload(start, end)
    elif argv[0] == "Simulation":
        start = argv[1]
        end = argv[2]
        m.simulation(start, end)


if __name__ == "__main__":
   main(sys.argv[1:])
