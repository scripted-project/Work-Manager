from modules.logs import Logger
from modules.server import Server
from flask import Flask, render_template, make_response

class Site:
    def __init__(self, app: Flask, logger: Logger, server: Server):
        
        clients = server.clients

        @app.route("/")
        def index():
            response = make_response(render_template("index.html"))
            logger.log(f"GET '/': index.html ({response.status_code})")
            return response
        
        @app.route("/dash")
        def dashboard():
            response = make_response(render_template("dashboard.html"))
            logger.log(f"GET '/dash': dashboard.html ({response.status_code})")
            return response
        
        @app.route("/users/<user>")
        def dashboard_withID(username: str):
            response = make_response(render_template("dashboard.html", username=username))
            logger.log(f"GET '/dash/{username}: dashboard.html [id = {username}] ({response.status_code})")
            return response
        
        @app.route("/test")
        def test():
            return render_template('test.html')