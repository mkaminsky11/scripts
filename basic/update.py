import subprocess

#DO BASIC UPGRADES
#=====================
subprocess.call("apt-get update -y".split())
subprocess.call("apt-get upgrade -y".split())
subprocess.call("apt-get autoremove -y".split())
subprocess.call("apt-get autoclean -y".split())

print "basic updates done! downloading tools!"

subprocess.call("apt-get install unattended-upgrades -y".split())
subprocess.call("dpkg-reconfigure -plow unattended-upgrades".split())
tools_array = ["libpam-cracklib", "nmap", "gufw", "rkhunter", "chkrootkit"]
tools = "apt-get install " + ' '.join([str(x) for x in tools_array]) + " -y"
subprocess.call(tools.split())

#UPDATE FIREFOX
#======================
print "tools downloaded! updating firefox!"
#it's happended that "sudo apt-get update firefox" doesn't work
subprocess.call("killall firefox".split())
subprocess.call("apt-get remove firefox -y".split())
subprocess.call("apt-get install firefox -y".split())

#RUN PROGRAMS
#==================
subprocess.call("software-properties-gtk".split())
subprocess.call("gufw")
subprocess.call("chkrootkit")

#UPDATE DIST
#===============
#you know, just because
print "updating dist....this may take a while"
subprocess.call("apt-get dist-upgrade -y".split())
