from flask import Flask, jsonify
from modules.logs import Logger

class API:
    def __init__(self, app: Flask, logger: Logger):
        @app.route('/api/test')
        def test():
            res = {"hello": """worldjhkjhnjnjkknjnjnjjjhjghhgfhgfrtderestrstrdtfdgfcgfcgfclglgkygyugkyugyugyugyugygkygkuyghkhghgkhuigjhgkgfjghfjytfjhgfjhfgjhgjghjgh"""}
            logger.log(f"GET '/api/test': {res}")
            return jsonify(res)