from flask import Flask
import logging
from modules.logs import Logger
from modules.site import Site
from modules.api import API

app = Flask(__name__)

unusedLog = logging.getLogger('werkzeug')
unusedLog.setLevel(logging.ERROR)

logger = Logger()

site = Site(app, logger)
api = API(app, logger)

if __name__ == "__main__":
    app.run()