const { PythonShell } = require('python-shell');
const path = require('path');

let appState = 0; //0 means stop
let keysAdded = 0;

function addNewRow(key, value){
  let th=document.createElement('th');
  th.scope="row";
  th.innerHTML = keysAdded+1;
  th.id="head"+keysAdded;

  let tdKey=document.createElement('td');
  tdKey.id="key"+keysAdded;
  tdKey.innerHTML = key;

  let tdValue=document.createElement('td');
  tdValue.id="value"+keysAdded;
  tdValue.innerHTML = value;

  let editButton=document.createElement('button');
  // editButton.inner
  editButton.innerHTML = "<i class='bi bi-pencil-square'></i>";
  editButton.className = 'edit-btn';
  const editId = keysAdded;
  editButton.addEventListener('click', function(){
    editKeyValue(editId, key, value);
  });

  let delButton=document.createElement('button');
  delButton.innerHTML = "<i class='bi bi-trash'>";
  delButton.className = "del-btn";
  const delId = keysAdded;
  delButton.addEventListener('click', function(){
    // console.log("dwdawd");
    delKeyValue(delId);
  });


  let tr=document.createElement('tr');
  tr.appendChild(th);
  tr.appendChild(tdKey);
  tr.appendChild(tdValue);
  tr.appendChild(editButton);
  tr.appendChild(delButton);
  tr.id="row"+keysAdded;

  keysAdded += 1;

  return tr;
}

function showKeyValueList(){
    let tbody=document.getElementById("key-value-list-tbody");
    //Get Key-Value List from db
    let list={
        "@name2": "Shubham Pal",
        "@name1": "Naman Jain"
    };
    for(let key in list){
        if(list.hasOwnProperty(key)){
            let tr=addNewRow(key, list[key]);
            tbody.appendChild(tr);
        }
    }
}

function delKeyValue(id){
  console.log(id);
  document.getElementById("row"+id).remove();
}

function editKeyValue(id){
  console.log("edddd");
  //Trigger edit modal
  document.getElementById("oldKey").value = document.getElementById("key"+id).innerHTML;
  document.getElementById("oldValue").value = document.getElementById("value"+id).innerHTML;

  let saveButton=document.getElementById("edit-save");
  saveButton.addEventListener('click', function(){
    editSaveKeyValue(id);
  });
  $("#editModal").modal();
}


function editSaveKeyValue(id) {
  console.log(id);
  // console.log(document.getElementById("key"+id).value);
  document.getElementById("key"+id).innerHTML = document.getElementById("oldKey").value;
  document.getElementById("value"+id).innerHTML = document.getElementById("oldValue").value;
}

function addNewKeyValue(){
    let tbody = document.getElementById("key-value-list-tbody");
    //Get Key-Value from User
    let key=document.getElementById("newKey").value;
    let value=document.getElementById("newValue").value;

    let tr=addNewRow(key, value);
    tbody.appendChild(tr);
    
    //clear input fields after submit
    document.getElementById("newKey").value='';
    document.getElementById("newValue").value='';
}

showKeyValueList();

function toggleAppState() {
    if (appState === 0) start();
    else stop();
    appState = 1 - appState;
}

function start() {
    let options = {
        scriptPath: path.join(__dirname, '../Backend/'),
        args: ['start']
    };
    PythonShell.run('main.py',options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });    
}


function stop() {
    let options = {
        scriptPath: path.join(__dirname, '../Backend/'),
        args: ['stop']
    };
    PythonShell.run('main.py',options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });  
}

// var editEleem = document.createElement('input');
// inputElement.type = "button"
// inputElement.addEventListener('click', function(){
//     const id = keysAdded;
//     edit(id);
// });

// var inputElement = document.createElement('input');
// inputElement.type = "button"
// inputElement.addEventListener('click', function(){
//     const id = keysAdded;
//     edit(id);
// });

// ​document.body.appendChild(inputElement);​


//   function noob() {
//     let python = require('child_process').spawn('python', ['./../main2.py']);
//     python.stdout.on('data', function (data) {
//       console.log("Python response: ", data.toString('utf8'));
//       result.textContent = data.toString('utf8');
//     });
  
//     python.stderr.on('data', (data) => {
//       console.error(`stderr: ${data}`);
//     });
  
//     python.on('close', (code) => {
//       console.log(`child process exited with code ${code}`);
//     });
  
//   }

// const path = require("path")

// function noob() {
//     console.log("Here");
//     const options = {
//         scriptPath: path.join(__dirname, '/../')
//     };

//     const pycode = new python('main2.py', options);
//     pycode.on('message', function(message){
//         swal(message);
//         console.log(message);
//     })
//     /*
//     python.run(scriptPath, (err, results)=>{
//         console.log('Scripted exeutes successfully!');
//     })
//     */
// }