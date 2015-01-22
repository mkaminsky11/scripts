var run = require("./../general.js").run;
var fs = require("fs");

//YOU'RE GOING TO BE EDITING /etc/pam.d/common-password, /etc/pam.d/common-auth, and /etc/login.defs
//=======================
//so, make some backups

run("cp /etc/pam.d/common-password /etc/pam.d/common-password-backup", function(){
  common_password(); //make edits
});
run("cp /etc/pam.d/common-auth /etc/pam.d/common-auth-backup", function(){
  common_auth(); //make edits
});
run("cp /etc/login.defs /etc/login_backup.defs", function(){
  login_defs(); //make edits
});

//COOL, SO ALL BACKUPS DONE
//============================
//now, let's edit
function common_password(){
  var text = fs.readFileSync('/etc/pam.d/common-password', 'utf8').split("\n"); //split into lines
  
  //OK, SO FIRST, NEED TO REPLACE THE LINE WITH [success=1 default=ignore] with password    [success=1 default=ignore]  pam_unix.so obscure use_authtok sha512 shadow
  for(var i = 0; i < text.length; i++){
    var line = text[i];
    if(line.indexOf("[success=1 default=ignore]") !== -1){
      text[i] = "password    [success=1 default=ignore]  pam_unix.so obscure use_authtok sha512 shadow"
    }
  }
  
  //THEN, ADD SOME LINES
  text.push("password    requisite           pam_cracklib.so retry=3 minlen=8 difok=3 reject_username minclass=3 maxrepeat=2 dcredit=1 ucredit=1 lcredit=1 ocredit=1");
  text.push("password    requisite           pam_pwhistory.so use_authtok remember=24 enforce_for_root");
  text = text.join("\n");
  
  fs.writeFileSync('/etc/pam.d/common-password', text, 'utf8');
  
}

function common_auth(){
  var text = fs.readFileSync('/etc/pam.d/common-password', 'utf8').split("\n"); //split into lines
  
  //NEED TO ADD auth    optional            pam_tally.so deny=5 unlock_time=900 onerr=fail audit even_deny_root_account silent
  text.push("auth    optional            pam_tally.so deny=5 unlock_time=900 onerr=fail audit even_deny_root_account silent");
  text = text.join("\n");
  
  fs.writeFileSync('/etc/pam.d/common-auth', text, 'utf8');
}

function login_defs(){
  var text = fs.readFileSync('/etc/login.defs', 'utf8').split("\n"); //split into lines
  
  //CHANGE SOME PASSWORD STUFF
  for(var i = 0; i < text.length; i++){
    var line= text[i];
    if(line.indexOf("PASS_MIN_DAYS") !== -1){
      text[i] = "PASS_MIN_DAYS 7";
    }
    else if(line.indexOf(PASS_MAX_DAYS"") !== -1){
      text[i] = PASS_MAX_DAYS 90"";
    }
    else if(line.indexOf("PASS_WARN_AGE") !== -1){
      text[i] = "PASS_WARN_AGE 14";
    }
  }
  
  text = text.join("\n");
  fs.writeFileSync('/etc/login.defs', text, 'utf8');
}
