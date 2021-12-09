'use strict';
var packager = require('electron-packager');
var options = {
    'arch': 'x64',
    'platform': 'win32',
    'dir': './',
    'app-copyright': 'Paulo Galdo',
    'app-version': '2.1.6',
    'asar': true,
    'icon': './icons.jpeg',
    'name': 'TierraDesktop',
    'out': './releases',
    'overwrite': true,
    'prune': true,
    'version': '1.3.4',
    'version-string': {
        'CompanyName': 'Paulo Galdo',
        'FileDescription': 'Smart Typer', /*This is what display windows on task manager, shortcut and process*/
        'OriginalFilename': 'TierraDesktop',
        'ProductName': 'Smart Typer',
        'InternalName': 'TierraDesktop'
    }
};
packager(options, function done_callback(err, appPaths) {
    console.log("Error: ", err);
    console.log("appPaths: ", appPaths);
});