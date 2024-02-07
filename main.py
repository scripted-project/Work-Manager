from flask import Flask
import logging
from modules.logs import Logger
from modules.site import Site
from modules.api import API
from modules.encryption import new_key
from modules.server import Server

app = Flask(__name__)
srv = Server(app)
app.secret_key = new_key(1024)

unusedLog = logging.getLogger('werkzeug')
unusedLog.setLevel(logging.ERROR)

users = {}

logger = Logger()

site = Site(app, logger, srv)
api = API(app, logger, srv)

if __name__ == "__main__":
    app.run(port=5001, debug=True, host='0.0.0.0')
    