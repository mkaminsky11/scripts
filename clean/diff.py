import subprocess

print "script starting..."

#LISTS OF STUFF ON CLEAN INSTALL
#====================
f = open(filename, 'r+')
clean = f.read().split("\n")

#FIRST, GET ALL THINGS INSTALLED ON THIS COMPUTER
#===================
p = subprocess.Popen("dpkg --get-selections | grep -v deinstall", stdout=subprocess.PIPE, shell=True)
out,erro = p.communicate()

installed = out.split("\n")
for line in installed:
    new_line = line[::-1].replace('llatsni', '', 1)[::-1].strip()
    if (new_line in clean) == False:
        print "You may want to remove: " + new_line
