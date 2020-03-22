import os

if os.path.isdir('os_exercises'):
  pass
else:
  os.mkdir('os_exercises')
os.chdir('os_exercises')

for i in range(1, int(input("How many files: ")) + 1):
  f = open(f'exercise_{i}.py', 'w')
  f.write(input('write something: '))
  f.close()

def unique_words(filename):
  t = open(filename).read().split()
  t = set(t)
  return len(t)

max = 0
maxFile = ""
for filename in os.listdir('.'):
  if unique_words(filename) > max:
    max = unique_words(filename)
    maxFile = filename
print(open(maxFile).read())


