import subprocess
import os.path

#FIRST GET ALL USERS
#=====================
# there's probably a better way to do this
p = subprocess.Popen("ls /home".split(), stdout=subprocess.PIPE)
output, err = p.communicate()
users_on_computer = output.split("\n")

if (os.path.exists("../admin.txt") == True and os.path.exists("../auth.txt") == True):
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
else:
    print "admin.txt or auth.txt do not exist"


# the above code needs serious work!!
# !!
# !!

#THEN LOCK ROOT
#=============
subprocess.call("passwd -l root".split())
print "root has been locked!"

#/etc/security/access.conf -:root: ALL EXCEPT LOCAL
if os.path.exists("/etc/security/access.conf") == True:
    with open("/etc/security/access.conf", "a") as myfile:
        myfile.write("\n-:root: ALL EXCEPT LOCAL")
    print "access.conf edited!"
else:
    print "/etc/security/access.conf not found!"

#LOCK GUEST
#===========
if os.path.exists("/etc/lightdm/lightdm.conf") == True:
    with open("/etc/lightdm/lightdm.conf", "a") as myfile:
        myfile.write("\nallow-guest=false")

    print "guest locked!"
else:
    print "/etc/lightdm/lightdm.conf does not exist"
