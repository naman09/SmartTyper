from pynput.keyboard import Key, KeyCode, Listener, Controller 
from Core.KeyboardTyper import KeyboardTyper
 
class Engine:
    def __init__(self, database):
        self._keyboard = Controller()
        self._keyboardtyper = KeyboardTyper()
        self._buffer = []
        self.database = database
        with Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            listener.join()
        
    def _is_valid_char(self, key):
        if key != Key.shift or key != Key.backspace or key != Key.enter or key != Key.space:
            return True
    
    def _is_delimiter(self,key):
        return key in [Key.space, Key.enter] 


    def _tokenize(self):
        token=''
        backspaces=0
        for key in self._buffer[::-1]:
            if key == Key.backspace:
                backspaces+=1
                
            if type(key) is KeyCode:
                if backspaces==-1:
                    token=str(key)[1]+token
                else:
                    backspaces-=1
            if type(key) is Key and self._is_delimiter(key):
                backspaces -= 1

            print("****", token)
            """Check if token is valid""" 
            if(len(token)!=0 and token[0]=='@'):
                print(token)
                self._type_if_present(token)
                return 

    #@ho     =>@ h o space tab enter backspace m e  

    def _type_if_present(self, word):
        if (value := self.database.get_value(word)) is not None:
            self._keyboardtyper.backspace(len(word)+1)
            self._keyboardtyper.type_string(value)

    def _on_press(self, key):
        """Gets all the key presses """
        print(f'{key} pressed and buffer: {self._buffer}')
        self._buffer.append(key)
        if self._is_delimiter(key):
            self._tokenize()
            

            

    def _on_release(self, key):
        # print('Key released: {0}'.format(key))
        if key == Key.esc:
            # Stop listener
            return False


    def _backspace(self,count):
        self._keyboardtyper.backspace(count)
