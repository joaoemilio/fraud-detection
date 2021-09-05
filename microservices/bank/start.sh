#/bin/bash
export ELASTIC_APM_SERVER_URL=https://fraud-detection.apm.southamerica-east1.gcp.elastic-cloud.com
export ELASTIC_APM_SECRET_TOKEN=t2MsG7UEb5UpCY0mF1
export ELASTICSEARCH_URL=https://fraud-detection.es.southamerica-east1.gcp.elastic-cloud.com:9243

cd src
/home/joao/.local/bin/gunicorn --config gunicorn.conf --log-config logging.conf -b :5000 server:app