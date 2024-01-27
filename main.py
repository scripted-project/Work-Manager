from modules.api import API
from modules.site import Site
from modules.logs import Logger
from flask import Flask
import logging

app = Flask(__name__)

app.logger.setLevel(logging.ERROR)
log = logging.getLogger('werkzeug')
log.disabled = True

logger = Logger()
api = API(app, logger)
site = Site(app, logger)

if __name__ == '__main__':
    app.run()