from flask import Flask
from json import dump
from modules.json import JSONFile

class Server:
    def __init__(self, app: Flask):
        self.clients = {} 
        self.handshakes = {}

        self._nextDashboardID = 0

    def newUser(self, name: str, password: str):
        self.clients[name] = {
            "password": password,
            "dashboards": []
        }

    def newDash(self, user: str):
        self.clients[user]["dashboards"].append(self._nextDashboardID)
        f = open(f"data/dashboards/{self._nextDashboardID}.json", 'x')
        
        data = {"id": self._nextDashboardID, "widgets": []}
        
        dump(data, f)

        self._nextDashboardID += 1
        