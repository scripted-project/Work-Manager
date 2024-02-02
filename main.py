from flask import Flask
import logging
from modules.logs import Logger
from modules.site import Site
from modules.api import API
from modules.encryption import new_key

app = Flask(__name__)
app.secret_key = new_key(1024)

unusedLog = logging.getLogger('werkzeug')
unusedLog.setLevel(logging.ERROR)

users = {}

shared = {
    "users": users,
    "clients": {}
}

logger = Logger()

site = Site(app, logger, shared)
api = API(app, logger, shared)

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
    