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
    fs.writeFile("test.txt", value, function(err) {
      if(err) {
          return console.log(err);
      }
  
      console.log("The file was saved!");
  }); 
  }
};