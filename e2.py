import os
import pyautogui

def ss():
    im = pyautogui.screenshot()
    
    temp_dir =os.environ['TEMP']
    
    im.save(temp_dir+"\ss1.png")
    #import os  
    #os.rename('ss1.png','ss1.txt')
