import subprocess

print "script starting..."

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
    elif ("pam_cracklib.so" in line) == True:
        text[i] = ""

text.append("password    requisite           pam_cracklib.so retry=3 minlen=8 difok=3 reject_username minclass=3 maxrepeat=2 dcredit=1 ucredit=1 lcredit=1 ocredit=1")
text.append("password    requisite           pam_pwhistory.so use_authtok remember=24 enforce_for_root")
text = '\n'.join([str(x) for x in text])
common_pass.write(text)
common_pass.close()

#EDITING common-auth
#=================
text = common_auth.read().strip("\n").split("\n")

text.append("password    requisite           pam_cracklib.so retry=3 minlen=8 difok=3 reject_username minclass=3 maxrepeat=2 dcredit=1 ucredit=1 lcredit=1 ocredit=1")
text = '\n'.join([str(x) for x in text])
common_auth.write(text)
common_auth.close()

#EDITING login
#=======================
text = login.read().strip("\n").split("\n")
for i, line in enumerate(text):
    if ("PASS_MIN_DAYS" in line) == True:
        text[i] = "PASS_MIN_DAYS 7"
    elif ("PASS_WARN_AGE" in line) == True:
        text[i] = "PASS_WARN_AGE 14"
    elif ("PASS_MAX_DAYS" in line) == True:
        text[i] = "PASS_MAX_DAYS 90"

text = '\n'.join([str(x) for x in text])
login.write(text)
login.close()
