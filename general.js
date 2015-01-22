var sys = require('sys')
var exec = require('child_process').exec;

exports.run = function(command, callback){
	var child = exec(command, function(err, stdout, stderr){
		callback(err);
	});
};