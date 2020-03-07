from flask import Flask, request
from github import Github
import numpy as np

GITHUB_TOKEN = 'Paste your Github API Token here'
NUMBER = 10

starred = {}

g = Github(GITHUB_TOKEN)

def getBunchOfrepos(name):
    repos = g.get_user(name).get_repos('all')
    repos = list(repos)[:NUMBER]
    np.random.shuffle(repos)
    return repos

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    counter = 0
    if request.method == 'GET':
        return "Repo starred so far : " + str(counter)

    if request.method == 'POST':
        req_data = request.get_json()
        name = req_data['sender']['login']
        auth_user = g.get_user()
        try:
            if req_data['action'] == 'created':
                repoList = getBunchOfrepos(name)
                for repo in repoList:
                    auth_user.add_to_starred(repo)
                    counter += 1
                starred[name] = [x for x in repoList]
            if req_data['action'] == 'deleted':
                repoList = starred[name]
                for repo in repoList:
                    auth_user.remove_from_starred(repo)
            return "Operation Successful"
        except:
            return "Random response"