var run = require("./../general.js").run;
var fs = require("fs");

//IT'S OBVIOUS WHAT THIS DOES. IT'S SPLIT OFF FROM THE REST SO YOU DON'T RUN IT BY ACCIDENT
//=======================
//you're welcome
run("passwd -dl root", function(){});
