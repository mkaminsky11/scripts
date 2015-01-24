import subprocess
import os.path

print "script starting..."

#DELETE ALL AUTHORIZED KEYS
#===================
proc = subprocess.Popen("rm -rf /home/*/.ssh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, erro = proc.communicate()

#FIRST, MAKE A BACKUP
#=======================
subprocess.call("cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup".split())

#THEN, READ IT
#=====================
file = open(" /etc/ssh/sshd_config","r+")
text = file.read().strip("\n").split("\n")

if os.path.exists("/etc/ssh/sshd_config") == True:
    #REMOVE POTENTIALLY OFFENDING LINES
    #==================
    for i, line in enumerate(text):
        if ("PermitEmptyPasswords" in line) == True:
            text[i] = ""
        elif ("PermitRootLogin" in line) == True:
            text[i] = ""
        elif ("UsePrivilegeSeparatio" in line) == True:
            text[i] = ""
        elif ("SyslogFacility" in line) == True:
            text[i] = ""
        elif ("LogLevel" in line) == True:
            text[i] = ""
        elif ("LoginGraceTime" in line) == True:
            text[i] = ""
        elif ("StrictModes" in line) == True:
            text[i] = ""
        elif ("ChallengeResponseAuthentication" in line) == True:
            text[i] = ""
        elif ("UsePAM" in line) == True:
            text[i] = ""
        elif ("Protocol" in line) == True:
            text[i] = ""
        elif ("DebianBanner" in line) == True:
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
    file.write(text)
    file.close()

    subprocess.call("service sshd restart".split())
    print text
else:
    print "/etc/ssh/sshd_config does not exist"
