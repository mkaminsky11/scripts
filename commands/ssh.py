import subprocess
import os.path

print "script starting..."

#DELETE ALL AUTHORIZED KEYS
#==========================
proc = subprocess.Popen("rm -rf /home/*/.ssh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, erro = proc.communicate()

#FIRST, MAKE A BACKUP
#=======================
subprocess.call("cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup".split())

#THEN, READ IT
#=====================

if os.path.exists("/etc/ssh/sshd_config") == True:
    file = open("/etc/ssh/sshd_config","r+")
    text = file.read().strip("\n").split("\n")

    #ADD CORRECT LINES
    #===================
    text.append("PermitEmptyPasswords no")
    text.append("PermitRootLogin no")
    text.append("UsePrivilegeSeparation yes")
    text.append("SyslogFacility AUTH")
    text.append("LogLevel INFO")
    text.append("LoginGraceTime 20")
    text.append("StrictModes yes")
    text.append("ChallengeResponseAuthentication yes")
    text.append("UsePAM yes")
    text.append("Protocol 2")
    text.append("DebianBanner no")

    #FINALLY, WRITE AND RESTART
    #======================
    text = '\n'.join([str(x) for x in text])
    file.write(text)
    file.close()

    subprocess.call("service sshd restart".split())
else:
    print "/etc/ssh/sshd_config does not exist"
