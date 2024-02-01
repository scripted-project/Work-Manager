from modules.logs import Logger
from modules.switches import Switch
from flask import Flask, make_response, request
from secrets import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

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
            body = request.json
            
            if "request-type" not in body: 
                return make_response({"code": 400, "description": "Bad Request"})
            
            switch = Switch(body["request-type"])