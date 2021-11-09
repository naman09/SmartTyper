class FileDB:
    def __init__(self):
        self._words = {'@home':'test'}
        self.i = 0

    def get_value(self,word):
        if word.lower() == '@home':
            self.i += 1
            self._words["@home"] = 'tet' + str(self.i)
        return self._words.get(word.lower())