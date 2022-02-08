from flask import Flask
from flask_restful import Api, Resource, reqparse

import datetime


app = Flask(__name__)
api = Api(app)

clipboard_data = {'text':'', 'timestamp':None}


class Clipboard(Resource):
    def get(self):
        return clipboard_data, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        args = parser.parse_args()

        now = datetime.date.today()

        clipboard_data = {'text': args['text'], 'timestamp': now.strftime('%m/%d/%Y, %H:%M:%S')}

        return clipboard_data, 201

    def delete(self):
        now = datetime.date.today()

        clipboard_data = {'text':'' , 'timestamp': now.strftime('%m/%d/%Y, %H:%M:%S')}

        return clipboard_data, 200


api.add_resource(Clipboard, '/api/clipboard')

app.run(host='localhost', port='9009')