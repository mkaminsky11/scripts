#GET VERSION
#==============
p = subprocess.Popen("lsb_release -r", stdout=subprocess.PIPE, shell=True)
out,erro = p.communicate()

#output as -> Release:      12.04
#or something similar
version = out.replace("Release:", "", 1).strip().replace(".","",1)

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
for index in range(0, len(installed)):
    #reverse it, remove reverse of "install", re-reverse it, then strip whitespace
    installed[index] = installed[index][::-1].replace("llatsni", "", 1)[::-1].strip()
installed_string = '\n'.join([str(x) for x in installed])

filename = "clean" + version + ".txt"
f = open(filename, 'r+')
f.seek(0)
f.write(installed_string)
f.truncate()
f.close()
