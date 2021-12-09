const path = require('path');
var child = require('child_process').execFile;
var executablePath = "./backend.exe";

function executeBackend(parameters) {
    child(executablePath, parameters, function(err, data) {
        if(err){
           console.error(err);
           return;
        }
        console.log(data.toString());
    });
}

function startApp() {
    executeBackend(["start"]);
}

function stopApp() {
    executeBackend(["stop"]);
}

export { startApp, stopApp };