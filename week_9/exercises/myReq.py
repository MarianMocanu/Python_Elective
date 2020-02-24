import requests

r = requests.get('https://api.github.com/users/' +
input('Enter you Git account name: ') + '/repos')
git = r.text.split('')
print(git)
print(git.index('clone_url'))
#print(git[5516])