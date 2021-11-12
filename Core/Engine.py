from pynput.keyboard import Key, KeyCode, Listener, Controller 
from Core.KeyboardTyper import KeyboardTyper
 
class Engine:
    def __init__(self, database):
        self._keyboard = Controller()
        self._keyboardtyper = KeyboardTyper()
        self._buffer = [] #list of keys
        self._prev_kv = (None,None)
        self.database = database
        self._python_typed = 0
        with Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            listener.join()
    
    def _is_delimiter(self,key):
        return type(key) is Key and key in [Key.space, Key.enter, Key.tab] 

    def _tokenize(self):
        token=''
        backspaces=0
        for key in self._buffer[::-1]:
            if key == Key.backspace:
                backspaces+=1
                
            if type(key) is KeyCode:
                if backspaces == 0:
                    token = str(key)[1] + token
                elif backspaces > 0:
                    backspaces -= 1
            if backspaces > 0 and self._is_delimiter(key):
                backspaces -= 1
            elif backspaces == 0 and self._is_delimiter(key):
                return (None, None)

            # print("****", token)
            """Check if token is valid""" 
            if len(token) != 0 and token[0] == '@': #Pattern Recognition
                # print(token)
                value = self._type_if_present(token) 
                if value is not None: #word found
                    return token, value

        return (None, None)

    def _type(self, wordRemoved, wordTyped):
        self._keyboardtyper.backspace(len(wordRemoved)) 
        self._keyboardtyper.type_string(wordTyped) #type word with extra space
        self._python_typed = len(wordRemoved) + len(wordTyped)
        self._buffer = []
        return wordTyped
    
    def _type_if_present(self, word):
        """Replace the word with its value and return the value"""
        if (value := self.database.get_value(word)) is not None:
            return self._type(word, value)
    
    def _is_backspace(self, key):
        return type(key) is Key and key == Key.backspace
    
    def _get_len(self, obj):
        if obj is None:
            return 0
        return len(obj)
        
    def _on_press(self, key):
        """Gets all the key presses """
        print(f'{key} pressed')
        if self._python_typed > 0:
            self._python_typed -= 1
            return
        self._buffer.append(key)
        print(f'buffer: {self._buffer}')
        print("$$$$$")
        print(self._prev_kv)
        if self._prev_kv is not None and self._prev_kv[1] is not None and self._is_backspace(key):
            print(self._prev_kv)
            #remove value
            #type token
            #remove token from buffer
            self._type(self._prev_kv[1][:-1], self._prev_kv[0])
            self._prev_kv = (None, None)

        # if self._is_delimiter(key):
        self._prev_kv = self._tokenize()
        print(self._prev_kv)

        #remove token,value from buffer

    def _on_release(self, key):
        # print('Key released: {0}'.format(key))
        if key == Key.esc:
            # Stop listener
            return False


    def _backspace(self,count):
        self._keyboardtyper.backspace(count)
