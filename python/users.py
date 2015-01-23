import subprocess

print "Cyberpatriot script starting..."

#FIRST GET ALL USERS
#=====================
p = subprocess.Popen("ls /home".split(), stdout=subprocess.PIPE)
output, err = p.communicate()
users_on_computer = output.split("\n")

admin_auth = open('../admin.txt', 'r').read().strip("\n").split("\n")
not_admin_auth = open('../auth.txt', 'r').read().strip("\n").split("\n")
