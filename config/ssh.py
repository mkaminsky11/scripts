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

    #REMOVE POTENTIALLY OFFENDING LINES
    for i in range(len(text)):
        line = text[i]
        if ("PermitEmptyPasswords" in line) == True:
            text[i] = ""
        if ("PermitRootLogin" in line) == True:
            text[i] = ""
        if ("UsePrivilegeSeparation" in line) == True:
            text[i] = ""
        if ("SyslogFacility" in line) == True:
            text[i] = ""
        if ("LogLevel" in line) == True:
            text[i] = ""
        if ("LoginGraceTime" in line) == True:
            text[i] = ""
        if ("StrictModes" in line) == True:
            text[i] = ""
        if ("ChallengeResponseAuthentication" in line) == True:
            text[i] = ""
        if ("UsePAM" in line) == True:
            text[i] = ""
        if ("Protocol" in line) == True:
            text[i] = ""
        if ("DebianBanner" in line) == True:
            text[i] = ""


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

    file.seek(0)
    file.write(text)
    file.truncate()
    file.close()

    subprocess.call("service sshd restart".split())
else:
    print "/etc/ssh/sshd_config does not exist"
