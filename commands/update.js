var run = require("./../general.js").run;

//DOES BASIC UPGRADES
//===================
run("apt-get update -y", function(){
	run("apt-get upgrade -y", function(){});
	run("apt-get dist-update -y", function(){});
});

console.log("basic updates done!");

//NOW OTHER THINGS
//==================
//latest firfox, etc
run("apt-get install libpam-cracklib nmap gufw rkhunter chkrootkit -y", function(){});
run("apt-get remove firefox -y", function(){
	run("apt-get install firefox -y", function(){});
});
