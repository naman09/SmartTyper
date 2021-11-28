const fs = require('fs/promises');
const {createWriteStream} = require('fs');

export default class DataAccess {

    constructor() {
        console.log("Creating Data Access Obj");
        this.dbFilePath = "../database.txt";
        
    }

    readFile() {
        return fs.readFile(this.dbFilePath).then(data => {
            this.entries = JSON.parse(data);
        }); 
    }

    writeToFile() {
        console.log(this.entries);
        const writer = createWriteStream(this.dbFilePath);
        writer.write(JSON.stringify(this.entries)); 
    } 
  
    //returns Id or null if already exists
    addEntry(entry) {
        console.log('Add Entry')
        if (this.isEntryPresent(entry)) return null;
        this.entries[entry.key] = entry.value;
        this.writeToFile();
        console.log('Entries '+this.entries);
        return entry.key;
    }
  
    //returns Id or null if not present
    updateEntry(entry) {
        console.log("Update Entry");
        if(!this.isEntryPresent(entry)) return null;
        this.entries[entry.key]=entry.value;
        this.writeToFile();
        return entry.key;
    }
    
    //get all key-value pairs
    getAllEntries() {
        console.log("Get All Entries");
        console.log(this.entries);
        return this.entries;
    }
    
    //returns boolean
    isEntryPresent(entry){
        return this.entries[entry.key] !== undefined;
    }
    
    //delete key-value pair and
    deleteEntry(entry) {
        if(!this.isEntryPresent(entry)) return;
        delete this.entries[entry.key];
        this.writeToFile();
    }
  }