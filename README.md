# SmartTyper
Detect personal info across whole OS, and provide smart typing functionalities.

`Note - packaged app is targeted for windows only. You can package app again with electron builder to run on another platform.`

### Installation
1. Download the [packaged app](https://drive.google.com/file/d/1W5-Cwma6X3qFzsetbzFIVF9iEYkoN68m/view?usp=sharing)
2. Unzip the file
3. Go to environment variables
4. Add new user variable
5. Name - `SECRET` and value - `mnxYXH3oxyyzCFrjBoS8FE5LKQlKepVgzVzk3kpc0Ac=`
6. Now run the smart-typer.exe in the unzipped folder

### Screenshots



### Packaging

1. Install electron builder
2. Create a folder name build, include icon file.
3. Update package.json. 
 * Add 2 new commands under scripts - 
      ```
      "pack": "electron-builder --dir",
      "dist": "electron-builder"
      ```
 * Add target build info.
      ```
      E.g.
      "build": {
        "appId": "st",
        "win": {
          "target": "squirrel",
          "icon": "build/icon.ico"
         }
       }
      ```
4. npm run dist
5. npm run pack

