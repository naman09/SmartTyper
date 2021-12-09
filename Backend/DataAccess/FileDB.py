import json
import os 
from cryptography.fernet import Fernet

class FileDB:
    def __init__(self):
        dir = os.path.dirname(__file__)
        # self._db_file_path = os.path.join(dir, '../../database.txt')
        self._db_file_path = 'C:/dev/Nodejs/electron Apps/electron-quick-start/database.txt'
        self._last_modified_time = ''
        self._initialize_from_file()

    def _initialize_from_file(self):
        print("Initializing from file...")
        with open(self._db_file_path) as f:
            fernet = Fernet(os.environ['SECRET'].encode())
            data = fernet.decrypt(f.read().encode()) #bcz file stores string instead of in byte format
            self._words = json.loads(data.decode())
            self._last_modified_time = os.path.getmtime(self._db_file_path)

    def _isModified(self):
        recent_update_time = os.path.getmtime(self._db_file_path)
        return recent_update_time != self._last_modified_time

    def get_value(self,word):
        if self._isModified(): 
            self._initialize_from_file()
        return self._words.get(word.lower())
