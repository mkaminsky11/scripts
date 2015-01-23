import subprocess

print "Cyberpatriot script starting..."

#FIRST GET ALL USERS
#=====================
p = subprocess.Popen("ls /home".split(), stdout=subprocess.PIPE)
output, err = p.communicate()
users_on_computer = output.split("\n")

#THEN READ USERS FROM TEXT FILE
#========================
admin_auth = open('../admin.txt', 'r').read().strip("\n").split("\n")
not_admin_auth = open('../auth.txt', 'r').read().strip("\n").split("\n")
all_auth = admin_auth + not_admin_auth

#COMPRARE THE TWO
#==================
for person in users_on_computer:
    if (person in all_auth) == False:
        #he's not in the authorized list
        print "YOU MAY WANT TO REMOVE: " + person

print "==============\nDON'T FORGET TO CHECK WHO IS AUTHORIZED TO BE AN ADMIN!"

#THEN LOCK ROOT
#=============
subprocess.call("passwd -l root".split())

print "root has been locked!"
