from modules.logs import Logger
from modules.server import Server
from flask import Flask, render_template, make_response, request

class Site:
    def __init__(self, app: Flask, logger: Logger, server: Server):
        
        clients = server.clients

        @app.route("/")
        def index():
            response = make_response(render_template("index.html"))
            logger.log(f"GET '/': index.html ({response.status_code})")
            return response
        
        @app.route("/dashboard")
        def dashboard():
            response = make_response(render_template("dashboard.html"))
            logger.log(f"GET '/dash': dashboard.html ({response.status_code})")
            return response
        
        @app.route("/login-signup")
        def login_signup():
            if request.method == 'POST': 
                #when the form is submitted
                username = request.form.get("username", None)
                password = request.form.get("password", None)
            elif request.method == 'GET':
                #when page needs to be rendered
                response = make_response(render_template("login-signup.html"))
                logger.log(f"GET '/login-signup': login-signup.html ({response.status_code})")
                return response

        @app.route("/test")
        def test():
            return render_template('test.html')