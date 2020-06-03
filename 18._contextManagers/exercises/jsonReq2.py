import json
import subprocess
import os
# subprocess.run(["pip", "install", "requests"])
import requests

with requests.get("https://api.github.com/orgs/python-elective-fall-2019/repos") as req:
    json_list = json.loads(req.text)
    for jsonItem in json_list:
        if jsonItem["name"] == "Lesson-09-context-managers":
            subprocess.run(["git", "clone", jsonItem["clone_url"]])
            for file in os.listdir(f"{jsonItem['name']}/code_examples"):
                if file.endswith(".ipynb"):
                    print(file)

