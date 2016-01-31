import subprocess

#####################
# TESTED, ALL GOOD! #
#####################

#DO BASIC UPGRADES
#=====================
subprocess.call("apt-get update -y".split())
subprocess.call("apt-get upgrade -y".split())
subprocess.call("apt-get autoremove -y".split())
subprocess.call("apt-get autoclean -y".split())

important_services = ["openssh-server", "samba", "telnetd"] # make sure that they are installed and updated

print("basic updates done! downloading tools!")

subprocess.call("apt-get install unattended-upgrades -y".split())
subprocess.call("dpkg-reconfigure -plow unattended-upgrades".split())
tools_array = ["libpam-cracklib", "nmap", "gufw", "rkhunter", "chkrootkit", "auditd", "bum", "clamtk"]
tools = "apt-get install " + ' '.join([str(x) for x in tools_array]) + " -y"
subprocess.call(tools.split())

#UPDATE FIREFOX
#======================
print("tools downloaded! updating firefox!")
#it's happended that "sudo apt-get update firefox" doesn't work
subprocess.call("killall firefox".split())
subprocess.call("apt-get remove firefox -y".split())
subprocess.call("apt-get install firefox -y".split())

#RUN PROGRAMS
#==================
subprocess.call("software-properties-gtk".split())
subprocess.call("gufw")
subprocess.call("chkrootkit")
subprocess.call("auditctl -e 1".split())

#CONFIGURE ANTIVIRUS
#====================
subprocess.call("freshclam".split()) #updates antivirus definitions
# subprocess.call("clamtk".split())

#UPDATE DIST
#===============
#you know, just because
print("updating dist....this may take a while")
subprocess.call("apt-get dist-upgrade -y".split())
