var run = require("./../general.js").run;

//DOES BASIC UPGRADES
//===================
run("apt-get update -y", function(){
	run("apt-get upgrade -y", function(){
		console.log("basic updates done! updating dist!");
		run("apt-get dist-upgrade -y", function(){
			next();
		});
	});
});

//NOW OTHER THINGS
//==================
//latest firfox, etc
function next(){
	console.log("downloading tools!")
	run("apt-get install libpam-cracklib nmap gufw rkhunter chkrootkit -y", function(){
		run("apt-get remove firefox -y", function(){
			run("apt-get install firefox -y", function(){});
		});
	});
}
