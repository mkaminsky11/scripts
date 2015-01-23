import subprocess

print "script starting..."

#REMOVE TELNET
#====================
subprocess.call("apt-get purge telnet -y".split())
