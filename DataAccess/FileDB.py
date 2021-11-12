class FileDB:
    def __init__(self):
        self._words = {'@pass1':'password','@user':'demonkinglollololroxx','@home':'test','@aadhaar':'XXXX-XXXXX-XXXX','@pan':'XXXXXXXXX','@adr1':'House No.X, Road Y','@adr2':'Delhi-1100XX','@phone':'9999999999','@name':'Shubham Pal', '@email':'namanjain9101999@gmail.com',
        '@lol':'lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll'}
        self.i = 0

    def _initialize_from_file(self):
        with open("database.txt") as f:
            for [key,value] in f.split():
                self._words[key] = value

    def get_value(self,word):
        # if word.lower() == '@home':
        #     self.i += 1
        #     self._words["@home"] = 'tet' + str(self.i)
        return self._words.get(word.lower())