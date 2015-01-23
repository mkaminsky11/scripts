# CYBERPATRIOT #
some cyberpatriot scripts to make things easier.

## INTRODUCTION

> #### WARNING!
> I am not responsible for ANYTHING that happens if you run this code. There could be bugs that delete stuff, mess things up, etc. I have tested this only on certain configurations. Also, if you get in trouble for using this, it's not my fault either. Tough beans for you.

###### Q: WHAT'S UP WITH auth.txt AND admin.txt?
######A: so, with the cyberpatriot competitions, you get a list of authorized users and the admins. there are always some users on the computer who either need to be removed or have their sudo access revoked. if you just list the users in auth.txt (authorized users who are not authorized admins) and admin.txt (authorized admins), one name per line, and run users.js, it will tell you what to do. Simple, right?

## REQUIREMENTS
* Ubuntu (tested on 12.04)
* Python installed

## HOW TO USE
```shell
sudo apt-get install git
git clone https://github.com/mkaminsky11/cyberpatriot.git
cd cyberpatriot
cd commands # has all of the commands to run
sudo python update.py #or whatever other command you want to run
```

## COMMANDS
Each of the commands do different things, so you can run those that fit the scenario you're dealing with. Just run the appropriate javascript files.

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

### ftp
configures ftp.

### users [done]
changes permissions, removes unauthorized users.

### lock_root [done]
this locks the root account. It's in its own file so that you don't run it by accident.

## LICENSE

> The MIT License (MIT)
>
> Copyright (c) 2015 Michael Kaminsky
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
