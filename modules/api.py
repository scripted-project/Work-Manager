from modules.logs import Logger
from flask import Flask, make_response, jsonify

class API:
    def __init__(self, app: Flask, logger: Logger):
        @app.route("/internal/api/test", methods=["GET"])
        def internalApiTest():
            data = {"message": "Hello World!"}
            response = make_response(data)
            logger.log(data)
            return response