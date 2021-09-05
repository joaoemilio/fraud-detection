from elasticapm.contrib.flask import ElasticAPM
from elasticsearch import Elasticsearch
from flask import Flask
from api import bp as api_bp
from Config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.elasticsearch = Elasticsearch(
        cloud_id= app.config['ES_CLOUD_ID'],
        http_auth=("elastic", app.config['ES_CLOUD_PASSWORD']),
    )

    app.register_blueprint(api_bp, url_prefix='/bank')
    apm = ElasticAPM(app)
    return app

app = create_app()
if __name__ == '__main__':
    app.run()
