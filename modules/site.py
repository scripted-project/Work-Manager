from modules.logs import Logger
from modules.server import Server
from flask import Flask, render_template, make_response, request, session, redirect, url_for

class Site:
    def __init__(self, app: Flask, logger: Logger, server: Server):
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
        
        @app.route("/login-signup", methods=["POST", "GET"])
        def login_signup():
            if request.method == 'POST': 
                username = request.form.get("username", None)
                password = request.form.get("password", None)
                login = request.form.get("login", False)
                signup = request.form.get("signup", False)
                if not username or not password: return

                if signup != False:
                    server.newUser(username, password)
                    server.newDash(username)
                if username not in server.clients: return
                if server.clients[username]["password"] != password: return

                session["username"] = username
                
                return redirect(f"{url_for('dashboard')}?id={server.clients[username]['dashboards'][0]}")
            elif request.method == 'GET':
                response = make_response(render_template("login-signup.html"))
                logger.log(f"GET '/login-signup': login-signup.html ({response.status_code})")
                return response

        @app.route("/test")
        def test():
            return render_template('test.html')