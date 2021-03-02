import subprocess

p1 = subprocess.run (["ls", "-la"])

print (p1.stdout)