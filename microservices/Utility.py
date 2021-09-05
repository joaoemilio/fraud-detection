from elasticsearch import helpers, Elasticsearch
import json 
from datetime import datetime, timezone 
import dateutil.parser as dtparser
import logging
from logging.handlers import TimedRotatingFileHandler
import traceback
import sys
class Utility:

    def __init__(self):
        self._load_config()
        self.es = Elasticsearch(    
            cloud_id= self.config["ES_CLOUD_ID"] ,
            http_auth=("elastic", self.config["ES_CLOUD_PASSWORD"])
        )

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                TimedRotatingFileHandler("logs/bankservice.log",
                                            when="d",
                                            interval=1,
                                            backupCount=7),
                logging.StreamHandler(sys.stdout)
            ]
        )

    def _load_config(self):
        jconfig = self.read_json( f"config.json" )
        self.config = jconfig

    def read_json(self, fname):
        with open(fname, 'r') as json_file:
            return json.load(json_file)

######################
# ELASTICSEARCH UTILS
######################

    def exists(self, iname, id):
        return self.es.exists( id=id, index=iname)

    def bulk_create(self, iname, data, partial=100):
        count = 1
        if not partial: partial = len(data)
        actions = []
        for k in data:
            action = { "_index": iname, "_source": data[k], "id": k }
            actions.append( action )
            if partial and count == partial:
                helpers.bulk(client=self.es,actions=actions)
                actions = []
                count = 0
            else:
                count += 1

        helpers.bulk(client=self.es,actions=actions)        

#################### 
# DATETIME UTILS
####################
    def get_ts(self, yyyymmdd):
        yyyymmdd = f'{yyyymmdd}'
        t = f'{yyyymmdd[0:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:8]}T00:00:00+00:00'
        return int(datetime.timestamp(dtparser.isoparse(t)))

    def current_milis(self):
        dt = datetime.now()
        return dt.microsecond        

    def write_json(self, obj, fname):
        with open(fname, 'w') as outfile:
            json.dump(obj, outfile)

    def get_iso_datetime(self, ts):
        dt = datetime.fromtimestamp(ts,tz=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M")

    def get_iso_datetime_sec(self, ts):
        dt = datetime.fromtimestamp(ts,tz=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%S")

#################### 
# LOGGING AND INSTRUMENTATION UTILS
####################
    def info(self, msg:str):
        logging.info(msg)
    
    def error(self, msg:str):
        logging.error(msg)

    def exception(self, msg: str, e:Exception):
        logging.exception(msg, e)

    def debug(self, msg:str):
        logging.debug(msg)

    def warm(self, msg:str):
        logging.warm(msg)        