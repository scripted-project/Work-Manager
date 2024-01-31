from flask import Flask
from modules.logs import Logger
from modules.site import Site
from modules.api import API

app = Flask(__name__)
logger = Logger()

site = Site(app, logger)
api = API(app, logger)

app.run()