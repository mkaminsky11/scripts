import subprocess
import os.path

print "script starting..."

#FIRST, MAKE A BACKUP
#=======================
subprocess.call("sudo apt-get install vsftpd -y".split()) #actually, first make sure that you have ftp
subprocess.call("cp /etc/vsftpd.conf /etc/vsftpd_backup.conf".split())

if os.path.exists("/etc/vsftpd.conf") == True:
    #THEN, READ IT
    #=====================
    file = open("/etc/vsftpd.conf","r+")
    text = file.read().strip("\n").split("\n")

    #ADD NEW LINES
    #====================
    text.append("anonymous_enable=NO")
    text.append("local_enable=YES")
    text.append("write_enable=YES ")
    text.append("chroot_local_user=YES")

    #FINALLY, WRITE AND RESTART
    #======================
    text = '\n'.join([str(x) for x in text])
    file.write(text)
    file.close()

    subprocess.call("service vsftpd restart".split())
else:
    print "/etc/vsftpd.conf does not exist!"
