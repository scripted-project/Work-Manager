from modules.logs import Logger
from modules.switches import Switch
from flask import Flask, make_response, request
from secrets import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import logging

class API:
    def __init__(self, app: Flask, logger: Logger, shared: dict):
        handshakes = {}
        self.nextHandshakeID = 1
        users = shared["users"]
        
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
        
        @app.route("/api/handshake")
        def handshake():
            key = ''.join(choice(ascii_lowercase + ascii_uppercase + digits + punctuation) for _ in range(16))
            data = {
                "code": 202,
                "description": "Accepted",
                "id": self.nextHandshakeID,
                "key": key,
                "channel": f"/api/channels/{self.nextHandshakeID}"
            }
            handshakes[self.nextHandshakeID] = key
            self.nextHandshakeID += 1
            
            response = make_response(data)
            logger.log(f"GET '/api/handshake': {data}")
            return response
        @app.route("/api/channels/<id>")
        def channel(id: int):
            try:
                body = request.json
                response = {}
                switch = Switch(body["request-type"])

                @switch.case("dashboard")
                def dashboard():
                    switch2 = Switch(request.method)

                    @switch.case("GET")
                    def get():
                        response["code"] = 202
                        response["description"] = "Accepted"
                        response["out"] = "out"

                @switch.default
                def default():
                    response["code"] = 400
                    response["description"] = "Bad Request"
                    response["out"] = "out"

                switch.execute()
                return make_response(response)
            except Exception as e:
                response = {"code": 400, "description": "Bad Request"}
                logger.log(f"POST '/api/channels/{id}' (with body {body}): {response}")
                logger.log(e, logging.ERROR)
                return make_response(response)