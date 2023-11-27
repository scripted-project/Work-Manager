from github import Github
from pprint import pprint
from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)
orgName = "scripted-project"
g = Github()

class Data(dict):
    def __init__(self):
        self.data = {
            "username":"",
            "password": "",
            "data": {
                "orgs": {},
                "repos": {}
            }
        }
    

def retrieve(username: str, target: str, data: dict):
    if target == "repos" or "repo":
        user = g.get_user(username)
        for repo in user.get_repos():
            #contents = []
            #for content in repo.get_contents(""):
            #    contents.append(content)
            data[repo] = {
                "full-name": repo.full_name,
                "description": repo.description,
                "date-created": repo.created_at,
                "last-push": repo.pushed_at,
                "home-page": repo.homepage,
                "main-language": repo.language,
            #    "contents": contents
            }
    """if target == "teams" or "team":
        org = g.get_organization(username)
        teams = org.get_teams()
        for team in teams:
            members = []
            for member in team.get_members():
                members.append(member)
            data[team] = {
                "name": team.name,
                "members": members
            }"""
    if target == "user" or "users":
        org = g.get_organization(username)
        for user in org.get_members():
            repos = []
            for repo in user.get_repos():
                repos.append(repo)
            data[user] = {
                "name": user.name,
                "repos": repos
            }


#retrieve(orgName, "users", data["members"])
#retrieve(orgName, "repos", data["repos"])


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method() == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        login = request.form.get("login", False)
        
        if not username:
            return render_template("index", error="Enter Username", username=username, password=password)
        if not password:
            return render_template("index.html", error="Enter Password", username=username, password=password)
        
        session["username"] = username
        session["password"] = password
        session["data"] = Data()
        return redirect(url_for("dashboard"))
    
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashoard.html")