from flask import Flask
from modules.json import JSON

class Server:
    def __init__(self, app: Flask):
        self.clients = {}
        self.handshakes = {}

        j = JSON('data.json')
        if j.data != None:
            for name, data in j.data: self.clients[name] = data

    def newUser(self, name: str, password: str):
        self.clients[name] = {
            "password": password,
            "dashboards": {}
        }