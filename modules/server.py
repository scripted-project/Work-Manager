from flask import Flask
from modules.json import JSON

class Server:
    def __init__(self, app: Flask):
        self.clients = {}
        self.handshakes = {}

        j = JSON('data.json')
        for name, data in j: self.clients[name] = data

    def newUser(self, name: str, password: str):
        self.clients[name] = {
            "password": password,
            "dashboards": {}
        }
    
