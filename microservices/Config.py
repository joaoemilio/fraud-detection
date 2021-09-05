import os
from Utility import Utility

class Config(object):

    util = Utility()
    _config = util.read_json("config.json")
    ES_CLOUD_ID = _config['ES_CLOUD_ID']
    ES_CLOUD_PASSWORD = _config['ES_CLOUD_PASSWORD']

    ELASTIC_APM = {
        'SERVICE_NAME': _config['ELASTIC_APM_SERVICE_NAME'],
        'SERVER_URL': _config['ELASTIC_APM_SERVER_URL'],
        'SECRET_TOKEN': _config['ELASTIC_APM_SECRET_TOKEN'],
        'SERVICE_VERSION': _config['ELASTIC_APM_SERVER_URL'],
    }
