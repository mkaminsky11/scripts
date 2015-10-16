# NOTES
## Things that are not done by the files (work in progress)

### 1. remember to check `visudo`
```shell
visudo
```
output may be something like:
```shell
root    ALL=(ALL) ALL
```
make sure that everything is ok. Check to make sure no `NOPASSWD`

### 2. make sure that all games are removed

### 3. if not needed, stop telnet
```shell
sudo service telnet stop
```

### 4. remove unecessary services
find them using `lsof -i -n -P`

### 5. check cron again
```shell
crontab -e
```
look if there are any things in `/etc/init.d` like "nc" (netcat)

### 6. remove all unauthorized users and admins
Check the `readme` and the users on the computer

### 7. check `/etc/rc0.d`

### 8. check `~/.bash_login` and `~/.bash_logout`

### 9. look at `/etc/hosts`
Defaults: 
```
127.0.0.1 localhost
127.0.1.1 ubuntu
```

Ignore all lines that have `ip6` in them, comment out everything else.

### 10. Uninstall not needed application from `Ubuntu Software Center -> Installed Software`

## Resources
+ [http://www.fdrseacadets.org/index_files/CPtraining/Unit_Eight.pdf](http://www.fdrseacadets.org/index_files/CPtraining/Unit_Eight.pdf)
+ [http://www.rjsystems.nl/en/2100-pam-debian.php](http://www.rjsystems.nl/en/2100-pam-debian.php)
+ [https://github.com/mike-bailey/CCDC-Scripts/blob/master/linux.sh](https://github.com/mike-bailey/CCDC-Scripts/blob/master/linux.sh)
+ [https://github.com/sumwonyuno/cp-lockdown](https://github.com/sumwonyuno/cp-lockdown)
+ [http://www.tecmint.com/apache-security-tips/](http://www.tecmint.com/apache-security-tips/)