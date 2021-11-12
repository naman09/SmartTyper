from pynput.keyboard import Key, Controller 

class KeyboardTyper:
    def __init__(self):
        self.keyboard = Controller()

    def hit(self, char): 
        self.keyboard.press(char)
        self.keyboard.release(char)

    def backspace(self,count):
        for i in range(count):
            self.keyboard.press(Key.backspace)
            self.keyboard.release(Key.backspace)

    def type_string(self, line):
        for char in line: 
            self.hit(char)