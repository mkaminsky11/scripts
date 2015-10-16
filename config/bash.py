import subprocess
import os.path

#CONFIGURES BASH STUFF

#TODO: maybe to all users?

#PREVENT TAMPERING WITH THESE FILES
#==================================
append_only = [".bash_history",".bash_profile",".bash_login",".profile",".bash_logout",".bashrc"]
for appends in append_only:
    subprocess.call(("chattr +a ~/" + appends).split()) #set to append only
if os.path.exists("~/.bashrc") == False:

    #CREATE IT
    #===========
    subprocesses.call("touch ~/.bashrc".split())
    
file = open("~/.bashrc","r+")
text = file.read().strip("\n").split("\n")
text.append("shopt -s histappend")
text.append('readonly PROMPT_COMMAND="history -a" ')
text.append("readonly HISTFILE")
text.append("readonly HISTFILESIZE")
text.append("readonly HISTSIZE")
text.append("readonly HISTCMD")
text.append("readonly HISTCONTROL")
text.append("readonly HISTIGNORE")

text = '\n'.join([str(x) for x in text])
file.seek(0)
file.write(text)
file.truncate()
file.close()

#DISABLE OTHER SHELLS
#=====================
subprocesses.call("chmod 750 csh".spit())
subprocesses.call("chmod 750 tcsh ".spit())
subprocesses.call("chmod 750 ksh".spit())
