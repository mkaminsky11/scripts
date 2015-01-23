import subprocess

print "Cyberpatriot script starting..."

#THIS LOCKS THE ROOT USER
#===================
#in a separate file to prevent accidents
subprocess.call("passwd -dl root".split())

print "root locked!"
