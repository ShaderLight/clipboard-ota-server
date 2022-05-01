from asyncio.windows_events import NULL
from flask import Flask
from flask_restful import Api, Resource, reqparse

import datetime
import logging

from modules.data_handling import DataHandler

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)

dh = DataHandler()
app = Flask(__name__)
api = Api(app)


class Clipboard(Resource):
    def get(self):
        logging.info("Received get request")
        return dh.retrieve(), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        args = parser.parse_args()

        logging.info("Reveived post request with content '{}'.".format(args))

        now = datetime.date.today()

        clipboard_data = {'text': args['text'], 'timestamp': now.strftime('%m/%d/%Y, %H:%M:%S')}
        
        dh.save(clipboard_data)

        return clipboard_data, 201

    def delete(self):
        logging.info("Received delete request")
        
        dh.clear()

        return None, 200


api.add_resource(Clipboard, '/api/clipboard')

app.run(host='localhost', port='9009')