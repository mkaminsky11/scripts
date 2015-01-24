import subprocess

print "script starting..."

#RUN THE MAIN ROUTE
#====================
subprocess.call("sudo python commands/update.py".split())
subprocess.call("sudo python commands/malware.py".split())
subprocess.call("sudo python commands/login.py".split())
subprocess.call("sudo python commands/users.py".split())
subprocess.call("sudo python commands/cron.py".split())
subprocess.call("sudo python commands/ssh.py".split())
subprocess.call("sudo python commands/kernel.py".split())
