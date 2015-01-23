import subprocess

print "Cyberpatriot script starting..."

#FIRST, MAKE A BACKUP
#=======================
subprocess.call("cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup".split())

#THEN, READ IT
#=====================
file = open(" /etc/ssh/sshd_config","r+")
text = file.read().strip("\n").split("\n")

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
text.append("")
text.append("")
text.append("")

'''
TODO:
=======
/etc/ssh/sshd_config
-----------------
PermitEmptyPasswords no
PermitRootLogin no
UsePrivilegeSeparation yes
SyslogFacility AUTH
LogLevel INFO
LoginGraceTime 120
StrictModes yes
ChallengeResponseAuthentication yes
UsePAM yes
Protocol 2
DebianBanner no
-----------------
then,
service sshd restart
-----------------
'''
