from modules.logs import Logger
from modules.switches import Switch
from modules.json import JSONFile
from modules.encryption import new_key
from modules.server import Server
from flask import Flask, make_response, request, url_for
from secrets import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import logging

class API:
    def __init__(self, app: Flask, logger: Logger, server: Server):
        @app.route("/internal/api/test/get", methods=["GET"])
        def testGET():
            data = {"message": "Hello World!"}
            response = make_response(data)
            logger.log(f"GET '/internal/api/test/get': {data}")
            return response
        @app.route("/internal/api/test/post")
        def testPOST():
            message = request.json["message"]
            data = {"message": f"Accepted Request! Requested: {message}", "code": 202}
            response = make_response(data)
            logger.log(f"POST '/internal/api/test/post' (with request: {request.json}): {data}")
            return response
        
        @app.route("/api/widgets/<id>", methods=["GET"])
        def getwidget(id: str):
            data = JSONFile(f'./data/widgets/{id}.json')
            if (data.data == None):
                responseData = {}
                response = make_response(responseData)
                response.status_code = 404
                return response
            else:
                responseData = {"data": data.data}
                response = make_response(responseData)
                response.status_code = 200
                return response
        @app.route("/api/users/<id>", methods=["GET"])
        def getuser(id: str):
            data = JSONFile(f'./data/users/{id}.json')
            if (data.data == None):
                responseData = {}
                response = make_response(responseData)
                response.status_code = 404
                return response
            else:
                responseData = {"data": data.data}
                response = make_response(responseData)
                response.status_code = 200
                return response