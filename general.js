//THIS IS GENERAL STUFF
//=========================

var sys = require('sys')
var exec = require('child_process').exec;

exports.run = function(command, callback){
	var child = exec(command, function(err, stdout, stderr){
		if(err){
			console.log("EXEC ERROR: " + err);
		}
		sys.puts(stdout);
		callback();
	});
};

exports.complex = function(command, callback){
	var child = exec(command, function(err, stdout, stderr){
		if(err){
			console.log("EXEC ERROR: " + err);
		}
	});
};
