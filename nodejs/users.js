var run = require("./../general.js").run;
var complex = require("./../general.js").complex;
var fs = require("fs");

/*
CONFIGURING USERS
========================
1. GET A LIST OF ALL USERS ON COMPUTER
2. READ auth.txt, IN WHICH A USER PASTED A LIST OF ALL THE NON-ADMIN USERS
3. READ admin.txt, IN WHICH A USER PASTED A LIST OF ALL ADMIN USERS
4. LIST ALL USERS NOT ON EITHER auth.txt OR ADMIN.txt
    "you should remove: testuser"
5. READ A LIST OF ALL THE ADMINS ON THE COMPUTER
6. LIST ALL ADMINS NOT ON admin.txt
    "testuser is not an admin"
*/
