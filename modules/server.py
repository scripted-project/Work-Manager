from flask import Flask

class Server:
    def __init__(self, app: Flask):
        self.clients = {}
        self.handshakes = {}

    def newUser(self, name: str, password: str):
        self.clients[name] = {"password": password}
    
    