const path = require('path');
const child = require('child_process').execFile;
const executablePath = path.join(__dirname, 'backend.exe');

let appState = 0; //0 means stop
function toggleAppState() {
    if (appState === 0) startApp();
    else stopApp();
    appState = 1 - appState;
}

function getState() {
    return appState;
}

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


