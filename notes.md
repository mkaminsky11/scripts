# NOTES
##### Things that are not done by the files (work in progress)

######1. remember to check `visudo`
```shell
visudo
```
output may be something like:
```shell
root    ALL=(ALL) ALL
```
make sure that everything is ok.

######2. make sure certain things are updated and installed
* bash (bash)
* ssh (openssh-server)
* samba (samba)
* telnet (telnetd)

######3. make sure that all games are removed

######4. if not needed, stop telnet
```shell
sudo service telnet stop
```

######5. remove unecessary services
find them using `lsof -i -n -P`

######6. check cron again
```shell
crontab -e
```
look if there are any things in `/etc/init.d` like "nc" (netcat)

######7. change update settings
Open update manager, go to `settings`, `updates`, and set checks to `daily`. Then, install all packages.


#### Resources
+ [http://www.fdrseacadets.org/index_files/CPtraining/Unit_Eight.pdf](http://www.fdrseacadets.org/index_files/CPtraining/Unit_Eight.pdf)
+ [http://www.rjsystems.nl/en/2100-pam-debian.php](http://www.rjsystems.nl/en/2100-pam-debian.php)
