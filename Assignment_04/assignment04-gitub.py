import requests
import json

url = "https://api.github.com/repos/StephenCaulfield/data-representation-coursework"

filename = "repos-public.json"

response = requests.get(url)
print(response.status_code)
repoJSON = response.json()


with open(filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)