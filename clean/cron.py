import subprocess

#####################
# TESTED, ALL GOOD! #
#####################

#LIST ALL CRON JOBS
#=====================
subprocess.call("crontab -l".split())

#LOOK IN /etc/
#=================
p = subprocess.Popen("ls /etc/cron*", stdout=subprocess.PIPE, shell=True)
out,erro = p.communicate()
print out

#LOOK IN rc.local
#=========================
p = subprocess.Popen("cat /etc/rc.local".split(), stdout=subprocess.PIPE)
output, err = p.communicate()
text = output.split("\n")

for line in text:
    if len(line) > 0 and line.strip(" ")[0] != "#" and line.strip(" ") != "exit 0" and line.strip(" ") != "":
        print("something is in /etc/rc.local ... you should check it out")
