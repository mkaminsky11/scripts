var run = require("./../general.js").run;
var complex = require("./../general.js").complex;
var fs = require("fs");

var users_on_comp = []; //all users on computer (excluding root)
var all_auth = []; //all authorized users (admin + no)
var admin_on_comp = []; //all admins on computer
var admin_auth = []; //all authorized admins
var not_admin_auth = []; //all authorized users not admins

//FIRST, GET ALL USERS
//==========================
complex("cd /home; ls", function(out){
    users_on_comp = out.split("\n");

    //THEN, READ DATA
    admin_auth = fs.readFileSync("../admin.txt",'utf8').trim().split("\n");
    not_admin_auth = fs.readFileSync("../auth.txt",'uft8').trim().split("\n");
    all_auth = admin_auth.concat(not_admin_auth);
    
    for(var i = 0; i < users_on_comp.length; i++){
        var user = users_on_comp[i];
        if(all_auth.indexOf(user) === -1){
            console.log("YOU MAY NEED TO REMOVE: " + user);
        }
    }
    
    //for now, will have to handle admin stuff on your own
    console.log("==============\nDON'T FORGET TO CHECK WHO IS AUTHORIZED TO BE AN ADMIN!");
});
