import DataAccess from './DataAccess.js';

let keysAdded = 0;

const dataAccessObj = new DataAccess();
dataAccessObj.readFile().then(() => {
  showKeyValueList();
});

function getKeyValue(id) {
  const key = document.getElementById("key" + id).innerHTML;
  const value = document.getElementById("value" + id).innerHTML;
  console.log(key, value);
  return { "key": key, "value": value };
}

function addNewRow(key, value) {
  let tdKey = document.createElement('td');
  tdKey.id = "key" + keysAdded;
  tdKey.innerHTML = key;

  let tdValue = document.createElement('td');
  tdValue.id = "value" + keysAdded;
  tdValue.innerHTML = value;

  let tdAction = document.createElement('td');

  let editButton = document.createElement('button');
  editButton.innerHTML = "<i class='bi bi-pencil-square'></i>";
  editButton.className = 'edit-btn';
  const editId = keysAdded;
  editButton.addEventListener('click', function () {
    editKeyValue(editId, key, value);
  });

  let delButton = document.createElement('button');
  delButton.innerHTML = "<i class='bi bi-trash'></i>";
  delButton.className = "del-btn";
  const delId = keysAdded;
  delButton.addEventListener('click', function () {
    // console.log("dwdawd");
    delKeyValue(delId);
  });
  tdAction.appendChild(editButton);
  tdAction.appendChild(delButton);


  let tr = document.createElement('tr');
  tr.appendChild(tdKey);
  tr.appendChild(tdValue);
  tr.appendChild(tdAction);
  tr.id = "row" + keysAdded;

  keysAdded += 1;

  return tr;
}

function showKeyValueList() {
  let tbody = document.getElementById("key-value-list-tbody");
  //Get Key-Value List from db
  let list = dataAccessObj.getAllEntries();
  for (let key in list) {
    if (list.hasOwnProperty(key)) {
      let tr = addNewRow(key, list[key]);
      tbody.appendChild(tr);
    }
  }
}

function delKeyValue(id) {
  console.log(id);
  dataAccessObj.deleteEntry(getKeyValue(id));
  document.getElementById("row" + id).remove();
}

function editKeyValue(id) {
  //Trigger edit modal
  const keyValue = getKeyValue(id);
  document.getElementById("oldKey").value = keyValue.key;
  document.getElementById("oldValue").value = keyValue.value;

  let saveButton = document.getElementById("edit-save");
  saveButton.addEventListener('click', function () {
    editSaveKeyValue(id);
  });
  $("#editModal").modal();
}

function editSaveKeyValue(id) {
  console.log(id);
  // console.log(document.getElementById("key"+id).value);
  //Update the table at UI
  document.getElementById("key" + id).innerHTML = document.getElementById("oldKey").value;
  document.getElementById("value" + id).innerHTML = document.getElementById("oldValue").value;

  dataAccessObj.updateEntry(getKeyValue(id));


}

function addNewKeyValue() {
  let tbody = document.getElementById("key-value-list-tbody");
  //Get Key-Value from User
  let key = document.getElementById("newKey").value;
  let value = document.getElementById("newValue").value;

  let tr = addNewRow(key, value);
  tbody.appendChild(tr);

  //clear input fields after submit
  document.getElementById("newKey").value = '';
  document.getElementById("newValue").value = '';

  dataAccessObj.addEntry({ "key": key, "value": value });
}

window.addNewKeyValue = addNewKeyValue;
window.toggleAppState = toggleAppState;