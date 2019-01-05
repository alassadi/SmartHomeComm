var firebase = require("firebase");
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var xhr = new XMLHttpRequest();
const fs = require('fs');

// Initialize Firebase
var config = {
  apiKey: "AIzaSyD8jSi9DH4omLmZVeTIFBCfr1Xw1DQGV2M",
  authDomain: "smarthome-3c6b9.firebaseapp.com",
  databaseURL: "https://smarthome-3c6b9.firebaseio.com",
  projectId: "smarthome-3c6b9",
  storageBucket: "smarthome-3c6b9.appspot.com",
  messagingSenderId: "227730898463"
};

firebase.initializeApp(config);
//retrieve the object
var database = firebase.database();

//listen to firebase changes
var deviceRef = database.ref("Devices");
deviceRef.on("child_changed", function (snapshot) {
  console.log(snapshot.key +" "+ snapshot.child('enabled').val());
  parse(snapshot.key, snapshot.child('enabled').val());
});

// send http request
const url = 'https://us-central1-smarthome-3c6b9.cloudfunctions.net/helloWorld';
xhr.open("GET", url);
xhr.send();
xhr.onreadystatechange = (e) => {
  console.log(xhr.responseText)
};

function parse(key, value) {
  if(key == "my9iXu6WvEgx5oNLLegs"){ // the light inside
    if (value==false){
      value = 8;
    }else if (value==true){
      value=7;
    }
  } else if (key == "ICYkFxoI0x2ng9NzGark"){ // burglar alarm
    if (value==false){
      value = 2;
    }else if (value==true){
      value=1;
    }
  //}else if (key == "NjF7valDGmHOPZrF0S9O"){ // fire alarm
    //if (value==false){
      //value = 4;
    //}else if (value==true){
      //value = 3;
    //}
    
    else if(key == "NjF7valDGmHOPZrF0S9O"){ // turn off the firealarm
        if(value==true){
            value = 4;
        }
    }


  }else if (key == "HrWTumcyQgNbcai78KAv"){ // lamp outside
    if (value==false){
      value = 6;
    }else if (value==true){
      value=5;
    }
  }else if (key == "eGtv1yzXNHPiOeCqdY81"){ //door
    value = 9; 
  }else if (key == "ORr9T5abPtJpeV6XdPw8"){ // temp outside
    value = 10;
  }else if (key == "y3BVqxWaMZOmmcEPunb6"){ //radiator
    if (value==false){
      value = 12;
    }else if (value==true){
      value=11;
    }
  }else if (key == "Check if burglar alarm is on"){ // burglar alarm
    value = 13
  }else if (key == "Check if fire alarm is on"){
    value = 14
  }else if (key == "Check if outside lamp is on"){
    value = 15
  }else if (key == "Check if indoor lamp is on"){
    value = 16
  }else if (key == "Check temperature inside (upstairs)"){
    value = 17
  }else if (key == "Check temperature inside (downstairs)"){
    value = 18
  }else if (key == "Check state of house (Fire)"){  
    value = 19
  }else if (key == "Check state of house (Water Leak)"){
    value = 20
  }else if (key == "Check state of house (Stove)"){
    value = 21
  }else if (key == "Check state of house (Window)"){
    value = 22
  }
  write(value);
};

function write(value){
  fs.writeFile("test.txt", value, function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
}); 
}