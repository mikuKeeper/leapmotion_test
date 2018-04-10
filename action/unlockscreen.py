from pynput.keyboard import Key, Controller
import time
import os
class UnlockScreen():
    def __init__(self):
        workdir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(workdir, '../data/lockpass')

        fb = open(filepath)
        self.keyboard = Controller()
        self.password = fb.readline().strip()

    def getPassword(self):
        return self.password

    def lightScreen(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        time.sleep(1.5)
  
    def pressPassword(self):
        for p in self.password:
            self.keyboard.press(getattr(Key,p))
            self.keyboard.release(getattr(Key,p))
            time.sleep(0.1)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def unlock(self):
        self.lightScreen()
        self.pressPassword()

            



if __name__ == '__main__':
    us = UnlockScreen()
    us.lightScreen()
    us.pressPassword()

