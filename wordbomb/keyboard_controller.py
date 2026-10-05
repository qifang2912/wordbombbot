import pyautogui
import time
import random


def type_word(word):
    pyautogui.click(800, 500)

    # Random reaction time
    time.sleep(random.uniform(0.03, 0.1))


    
    pyautogui.write(word, interval=0.06)

    pyautogui.press('enter')