import requests
import subprocess

r = requests.get('https://api.github.com/users/' +
                 input('Enter you Git account name: ') + '/repos')
git = r.text
git_list = git.split('"')
git_url = git_list[git_list.index('clone_url') + 2]
print(git_url)

subprocess.run(['git', 'clone', git_url])
