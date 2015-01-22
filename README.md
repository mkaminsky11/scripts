# CYBERPATRIOT #
some cyberpatriot scripts to make things easier.

<blockquote>
Q: WHY TWO VERSIONS?
<br/>A: because I can.

<br/><br/>Q: WHAT'S UP WITH auth.txt AND admin.txt?
<br/>A: so, with the cyberpatriot competitions, you get a list of authorized users and the admins. there are always some users on the computer who either need to be removed or have their sudo access revoked. if you just list the users in auth.txt (authorized users who are not authorized admins) and admin.txt (authorized admins), one name per line, and run users.js, it will tell you what to do. Simple, right?
</blockquote>

## NODE.JS version
```shell
sudo apt-get install nodejs
node update.js #or whatever other file you want
```

## SHELL version
<blockquote>
I have not started working on the shell version yet....
</blockquote>
```shell
chmod +x update.sh #whatever file
./update.sh
```

### update [done]
updates things. pretty simple.

### ssh
configures ssh, sshd, etc.

### samba
configures samba

### login [done]
configures login stuff, like password length, root login, etc.

### malware [done]
scans for malware and other nasty stuff.

### telnet
configures telnet.

### users
changes permissions, removes unauthorized users.

### lock_root [done]
this locks the root account. It's in its own file so that you don't run it by accident.
