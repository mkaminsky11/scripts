import subprocess

print "Cyberpatriot script starting..."

#YOU'RE GOING TO BE EDITING /etc/pam.d/common-password, /etc/pam.d/common-auth, and /etc/login.defs
#=======================
#so, make some backups
subprocess.call("cp /etc/pam.d/common-password /etc/pam.d/common-password-backup".split())
subprocess.call("cp /etc/pam.d/common-auth /etc/pam.d/common-auth-backup".split())
subprocess.call("cp /etc/login.defs /etc/login_backup.defs".split())

#PREPARE FOR EDITING
#===================
common_pass = open("/etc/pam.d/common-password","r+")
common_auth = open("/etc/pam.d/common-auth","r+")
login = open("/etc/login.defs","r+")

#EDITING common-password
#=======================
text = common_pass.read().strip("\n").split("\n")
for i, line in enumerate(text):
    if ("[success=1 default=ignore]" in line) == True:
        text[i] = "password    [success=1 default=ignore]  pam_unix.so obscure use_authtok sha512 shadow"

text.append("password    requisite           pam_cracklib.so retry=3 minlen=8 difok=3 reject_username minclass=3 maxrepeat=2 dcredit=1 ucredit=1 lcredit=1 ocredit=1")
text.append("password    requisite           pam_pwhistory.so use_authtok remember=24 enforce_for_root")

text = '\n'.join([str(x) for x in text])
