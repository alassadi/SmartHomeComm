const fs = require('fs');

console.log("test")

fs.writeFile("test.txt", "5", function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
}); 