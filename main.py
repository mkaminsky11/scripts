import subprocess

print "script starting..."

#RUN THE MAIN ROUTE
#====================
subprocess.call("sudo python basic/update.py".split())
subprocess.call("sudo python clean/malware.py".split())
subprocess.call("sudo python basic/login.py".split())
subprocess.call("sudo python basic/users.py".split())
subprocess.call("sudo python clean/cron.py".split())
subprocess.call("sudo python config/ssh.py".split())
subprocess.call("sudo python clean/kernel.py".split())
