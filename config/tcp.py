import subprocess
import os.path

#####################
# TESTED, ALL GOOD! #
#####################

#FIRST, MAKE A BACKUP
#=======================
subprocess.call("cp /etc/sysctl.conf /etc/sysctl_conf_backup".split())

#THEN, READ IT
#=====================

if os.path.exists("/etc/sysctl.conf") == True:
    file = open("/etc/sysctl.conf","r+")
    text = file.read().strip("\n").split("\n")

    #ADD CORRECT LINES
    #===================
    text.append("net.ipv4.tcp_syncookies = 1")

    #FINALLY, WRITE AND RESTART
    #======================
    text = '\n'.join([str(x) for x in text])

    file.seek(0)
    file.write(text)
    file.truncate()
    file.close()

    subprocess.call("sysctl -p".split())
else:
    print("/etc/sysctl.conf does not exist")
