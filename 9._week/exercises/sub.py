import subprocess
import os
print(subprocess.run('ls'))

#print(subprocess.run(['mkdir', 'ooo']))
os.chdir('ooo')
#subprocess.run(['git', 'clone', 'https://github.com/Python-Elective-Spring-2020/introduction-to-python.git'])
os.chdir('..')
print(subprocess.run(['rm', '-r', 'ooo']))