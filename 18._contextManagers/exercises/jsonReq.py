# import subprocess
# subprocess.run(["pip", "install", "requests"])

import requests, json

with requests.get("https://api.github.com/orgs/python-elective-fall-2019/repos") as req:
    json_list = json.loads(req.text)
    f = open("names.txt", "w")
    for jsonItem in json_list:
        f.write(jsonItem["name"] + "\n")
    f.close()