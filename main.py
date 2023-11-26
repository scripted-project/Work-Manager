from github import Github
from pprint import pprint
from flask import Flask, request

app = Flask(__name__)
orgName = "scripted-project"
data = {
    "members": {},
    "repos": {},
    "teams": {}
}

g = Github()

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


retrieve(orgName, "users", data["members"])
retrieve(orgName, "repos", data["repos"])

@app.route("/")
def home():
    if request.method() == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        login = request.form.get("login")