var run = require("./../general.js").run;

//DOES BASIC UPGRADES
//===================
run("apt-get update -y", function(err){
	if(err){
		console.log(err);
	}
	
	run("apt-get upgrade -y", function(err){
		if(err){
			console.log(err);
		}
	});
	run("apt-get dist-update -y", function(err){
		if(err){
			console.log(err);
		}
	});
});

console.log("basic updates done!");

//NOW OTHER THINGS
//==================
//latest firfox, etc
run("apt-get install libpam-cracklib nmap gufw -y", function(err){
	if(err){
		console.log(err);
	}
});
run("apt-get remove firefox -y", function(err){
	if(err){
		console.log(err);
	}
	run("apt-get install firefox -y", function(err){
		if(err){
			console.log(err);
		}
	});
});