from github import Github
from pprint import pprint

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
def explore(data: dict):
    current = data
    layers = 0
    while True:
        layers += 1
        print("Current Dictionary:")
        for key, value in current.items():
            if layers > 2:
                print(f"{key}: {value}")
            else:
                print(f"{key}")
        userInput = input()
        
        if userInput == "exit":
            break
        if userInput in current and isinstance(current[userInput], dict):
            current = current[userInput]
        else:
            print("Invalid")
    

retrieve(orgName, "users", data["members"])
retrieve(orgName, "repos", data["repos"])

if __name__ == "__main__":
    explore(data)