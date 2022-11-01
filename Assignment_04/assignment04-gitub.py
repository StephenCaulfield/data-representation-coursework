import requests
from github import Github
from config import config as cfg


apikey = cfg["githubkey"]

g = Github(apikey)

repo = g.get_repo("StephenCaulfield/aprivateone")

print(repo.clone_url)

fileinfo= repo.get_contents("test.txt")
urlOfFile = fileinfo.download_url

print(urlOfFile)

response = requests.get(urlOfFile)
contentofFile = response.text
print(contentofFile)

newContents = contentofFile.replace("Andrew", "Stephen")

print(newContents)

gitHubResponse = repo.update_file(fileinfo.path, "updated by prog", newContents, fileinfo.sha)

print(gitHubResponse)