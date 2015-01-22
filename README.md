# CYBERPATRIOT #
some cyberpatriot scripts to make things easier.

<blockquote>
WARNING: I am not responsible for ANYTHING that happens if you run this code. There could be bugs that delete stuff, mess things up, etc. I have tested this only on certain configurations. Also, if you get in trouble for using this, it's not my fault either. Tough beans for you.
</blockquote>

Q: WHAT'S UP WITH auth.txt AND admin.txt?
A: so, with the cyberpatriot competitions, you get a list of authorized users and the admins. there are always some users on the computer who either need to be removed or have their sudo access revoked. if you just list the users in auth.txt (authorized users who are not authorized admins) and admin.txt (authorized admins), one name per line, and run users.js, it will tell you what to do. Simple, right?

## HOW TO USE
```shell
sudo apt-get install nodejs
git clone https://github.com/mkaminsky11/cyberpatriot.git
cd cyberpatriot
cd commands # has all of the commands to run
node update.js # or whatever other file you want
```

Each of the commands do different things, so you can run those that fit the scenario you're dealing with.

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
