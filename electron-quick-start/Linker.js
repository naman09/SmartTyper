const { PythonShell } = require('python-shell');
const path = require('path');
function startApp() {
    let options = {
        scriptPath: path.join(__dirname, '../Backend/'),
        args: ['start']
    };
    PythonShell.run('main.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });
}


function stopApp() {
    let options = {
        scriptPath: path.join(__dirname, '../Backend/'),
        args: ['stop']
    };
    PythonShell.run('main.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });
}

export { startApp, stopApp };