# import python packages
import requests
import json
from github import Github
from githubconfig import config as cfg

# name of the file which will be created
filename = "repos-github.json"

# to read data from a repository
url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation'

# request to get information from the repository
response = requests.get(url)
# print the status code of the response to check if it works
print(response.status_code)
# get the response in a json file
repoJSON = response.json()

# create and open a json file with information from the repository
with open (filename, 'w') as fp:
    json.dump(repoJSON, fp, indent = 4)

apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)

for repo in g.get_user().get_repos():
 print(repo.name)