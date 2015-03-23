import subprocess

print "script starting..."

#RUN THE MAIN ROUTE
#====================
# probably best to run them individually
# some of them have output that you want to read
subprocess.call("sudo python basic/update.py".split()) #updates packages
subprocess.call("sudo python clean/malware.py".split())#cleans away bad things
subprocess.call("sudo python basic/login.py".split())  #edits login requirements
subprocess.call("sudo python basic/users.py".split())  #checks users
subprocess.call("sudo python clean/cron.py".split())   #removes cron jobs
subprocess.call("sudo python config/ssh.py".split())   #configures ssh
subprocess.call("sudo python clean/kernel.py".split()) #configures the kernel (just because)
subprocess.call("sudo python clean/diff.py".split())   #checks if any programs that are not there by default are installed
