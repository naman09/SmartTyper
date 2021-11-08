class FileDB:
    def __init__(self):
        self.words = {'@home':'test'}

    def get_value(self,word):
        return self.words.get(word.lower())