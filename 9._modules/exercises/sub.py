import subprocess
import os
print(subprocess.run('ls'))

#print(subprocess.run(['mkdir', 'ooo']))
os.chdir('ooo')
#subprocess.run(['git', 'clone', 'a'])
os.chdir('..')
print(subprocess.run(['rm', '-r', 'ooo']))