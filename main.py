import subprocess

print("script starting...")

#RUN THE MAIN ROUTE
#====================
# probably best to run them individually
# some of them have output that you want to read


files = ["basic/update", "clean/malware", "basic/login", "basic/users", "clean/cron", "config/ssh", "clean/kernel", "clean/diff", "config/bash"]

for i in range(0, len(files)):
	subprocess.call((files[i] + ".py").split())
