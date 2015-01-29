import subprocess

#GET VERSION
#==============
p = subprocess.Popen("lsb_release -r", stdout=subprocess.PIPE, shell=True)
out,erro = p.communicate()

#output as -> Release:      12.04
#or something similar
version = out.replace("Release:", "", 1).strip().replace(".","",1)

#LISTS OF STUFF ON CLEAN INSTALL
#====================
filename = "clean" + version + ".txt"
if os.path.exists(filename) == False:
    filename = "clean1204.txt"

f = open(filename, "r+")
clean = f.read().split("\n")

#FIRST, GET ALL THINGS INSTALLED ON THIS COMPUTER
#===================
p = subprocess.Popen("dpkg --get-selections | grep -v deinstall", stdout=subprocess.PIPE, shell=True)
out,erro = p.communicate()

installed = out.split("\n")
#will output something like ->
#some_package           install
#another_package        install
#pack                   install
#p                      install
for line in installed:
    #reverse it, remove reverse of "install", re-reverse it, then strip whitespace
    new_line = line[::-1].replace("llatsni", "", 1)[::-1].strip()
    if (new_line in clean) == False:
        print "You may want to remove: " + new_line
