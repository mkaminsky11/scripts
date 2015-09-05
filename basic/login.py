import subprocess
import os.path

# THIS IS PROBABLY THE MOST IMPORTANT
# AUTOCONFIGURES PASSWORD CONFIG

#####################
# TESTED, ALL GOOD! #
#####################

#YOU'RE GOING TO BE EDITING /etc/pam.d/common-password, /etc/pam.d/common-auth, and /etc/login.defs
#=======================
#so, make some backups
subprocess.call("cp /etc/pam.d/common-password /etc/pam.d/common-password-backup".split())
subprocess.call("cp /etc/pam.d/common-auth /etc/pam.d/common-auth-backup".split())
subprocess.call("cp /etc/login.defs /etc/login_backup.defs".split())

#PREPARE FOR EDITING
#===================
#read both files
common_pass = open("/etc/pam.d/common-password","r+")
common_auth = open("/etc/pam.d/common-auth","r+")
login = open("/etc/login.defs","r+")

#EDITING common-password
#=======================
text = common_pass.read().strip("\n").split("\n")
#remove potentially offending lines
for i in range(len(text)):
    line = text[i]
    if ("password" in line) == True:
        text[i] = ""

text.append("password    [success=1 default=ignore]  pam_unix.so obscure use_authtok sha512 shadow remeber=5")
text.append("password    requisite           pam_cracklib.so retry=3 minlen=8 difok=3 reject_username minclass=3 maxrepeat=2 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1")
text.append("password    requisite           pam_pwhistory.so use_authtok remember=24 enforce_for_root")
text = '\n'.join([str(x) for x in text])
#update text
common_pass.seek(0)
common_pass.write(text)
common_pass.truncate()
common_pass.close()

#EDITING common-auth
#=================
text = common_auth.read().strip("\n").split("\n")
text.append("auth required pam_tally.so deny=5 unlock_time=900 onerr=fail audit even_deny_root_account silent")
text = "\n".join([str(x) for x in text])

common_auth.seek(0)
common_auth.write(text)
common_auth.truncate()
common_auth.close()

#EDITING login
#=======================
text = login.read().strip("\n").split("\n")
for i in range(len(text)):
    line = text[i]
    if ("PASS_MIN_DAYS" in line) == True:
        text[i] = "PASS_MIN_DAYS 10"
    elif ("PASS_WARN_AGE" in line) == True:
        text[i] = "PASS_WARN_AGE 7"
    elif ("PASS_MAX_DAYS" in line) == True:
        text[i] = "PASS_MAX_DAYS 90"

text = "\n".join([str(x) for x in text])

login.seek(0)
login.write(text)
login.truncate()
login.close()

#LOCK DOWN ON /etc/shadow
#====================
subprocess.call("chmod o-r /etc/shadow".split())
