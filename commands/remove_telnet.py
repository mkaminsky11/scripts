import subprocess

print "script starting..."

#REMOVE TELNET
#====================
subprocess.call("apt-get purge telnet -y".split())
subprocess.call("apt-get autoremove -y".split())
subprocess.call("apt-get autoclean -y".split())
