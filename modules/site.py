from modules.logs import Logger
from flask import Flask, render_template, make_response

class Site:
    def __init__(self, app: Flask, logger: Logger, shared: dict):
        
        @app.route("/")
        def index():
            response = make_response(render_template("index.html"))
            logger.log(f"GET '/': index.html {response.status_code}")
            return response
        
