import subprocess
import os.path

#####################
# TESTED, ALL GOOD! #
#####################

# NOTE: REMOVED CODE THAT COMPARES readme.txt TO ACTUAL USERS
# it got very clumsy, and didn't work correctly

#THEN LOCK ROOT
#=============
subprocess.call("passwd -l root".split())
print("root has been locked!")

#/etc/security/access.conf -:root: ALL EXCEPT LOCAL
if os.path.exists("/etc/security/access.conf") == True:
    with open("/etc/security/access.conf", "a") as myfile:
        myfile.write("\n-:root: ALL EXCEPT LOCAL")
    print("access.conf edited!")
else:
    print("/etc/security/access.conf not found!")

#LOCK GUEST
#===========
if os.path.exists("/etc/lightdm/lightdm.conf") == True:
    with open("/etc/lightdm/lightdm.conf", "a") as myfile:
        myfile.write("\nallow-guest=false")

    print("guest locked!")
else:
    print("/etc/lightdm/lightdm.conf does not exist")


# TODO:
# python -c "import crypt, getpass, pwd; print crypt.crypt('password', '\$6\$SALTsalt\$')"
