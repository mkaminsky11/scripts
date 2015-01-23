import subprocess

print "Cyberpatriot script starting..."

#START UFW
#====================
subprocess.call("ufw allow ssh".split())
subprocess.call("ufw allow http".split())
subprocess.call("ufw deny 23".split())
subprocess.call("ufw default deny".split())
subprocess.call("ufw enable".split())
subprocess.call("ufw limit OpenSSH".split())
