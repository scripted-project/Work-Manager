from flask import Flask, render_template, make_response
from modules.logs import Logger

class Site:
    def __init__(self, app: Flask, logger: Logger):
        @app.route('/')
        def home():
            res = make_response(render_template('index.html'))
            logger.log(f"GET '/': index.html ({res._status_code})")
            return res