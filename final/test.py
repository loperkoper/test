#This script locates the image stickman.png in the region we give it and tell you if it can see it

from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
sleep(5)
try:
    if pyautogui.locateOnScreen('account.png') != None:
            pyautogui.click('account.png')
            sleep(0.5)
except:
    sleep(2)
    if pyautogui.locateOnScreen('account.png') != None:
            pyautogui.click('account.png')
            sleep(0.5)
try:

    if pyautogui.locateOnScreen('account2.png') != None:
            pyautogui.click('account2.png')
            sleep(0.5)
except:
    sleep(2)
    if pyautogui.locateOnScreen('account2.png') != None:
            pyautogui.click('account2.png')
            sleep(0.5)

try:

    if pyautogui.locateOnScreen('account3.png') != None:
            pyautogui.click('account3.png')
            sleep(1.5)
except:
    sleep(2)
    if pyautogui.locateOnScreen('account3.png') != None:
            pyautogui.click('account3.png')
            sleep(1.5)
sleep(2)
keyboard.press('1')
keyboard.release('1')
sleep(2)
try:

    if pyautogui.locateOnScreen('account4.png') != None:
            pyautogui.click('account4.png')
            pyautogui.click('account4.png')
            sleep(1.5)
except:
    sleep(2)
    if pyautogui.locateOnScreen('account4.png', confidence=0.8) != None:
            pyautogui.click('account4.png')
            pyautogui.click('account4.png')
            sleep(1.5)
def make_account():
    while i < 3:
        i = 2
        sleep(1)
        try:
            if pyautogui.locateOnScreen('account5.png') != None:
                pyautogui.click('account5.png')
                sleep(1.5)
        except:
            sleep(2)
            if pyautogui.locateOnScreen('account5.png') != None:
                pyautogui.click('account5.png')
                sleep(1.5)
        try:

            if pyautogui.locateOnScreen('account2.png') != None:
                    pyautogui.click('account2.png')
                    sleep(0.5)
        except:
            sleep(2)
            if pyautogui.locateOnScreen('account2.png') != None:
                    pyautogui.click('account2.png')
                    sleep(0.5)

        try:

            if pyautogui.locateOnScreen('account3.png') != None:
                    pyautogui.click('account3.png')
                    sleep(1.5)
        except:
            sleep(2)
            if pyautogui.locateOnScreen('account3.png') != None:
                    pyautogui.click('account3.png')
                    sleep(1.5)
        sleep(1)
        keyboard.press('1')
        keyboard.release('1')
        sleep(3)
        try:

            if pyautogui.locateOnScreen('account4.png', confidence=0.8) != None:
                    pyautogui.click('account4.png')
                    pyautogui.click('account4.png')
                    sleep(1.5)
        except:
            sleep(2)
            if pyautogui.locateOnScreen('account4.png', confidence=0.8) != None:
                    pyautogui.click('account4.png')
                    sleep(1.5)
        i = i+1
while 1:
    time.sleep(0.4)
    if pyautogui.locateOnScreen('close.png') != None:
            pyautogui.click('close.png')
            #print("I can see so click")
            time.sleep(0.5)
    elif pyautogui.locateOnScreen('Untitled.png', confidence=0.5) != None:
        pyautogui.click('Untitled.png')
        print("I can see so click")
        time.sleep(0.5)
    elif pyautogui.locateOnScreen('captcha.png') != None: 
        pyautogui.keyDown("ctrl")
        pyautogui.press('r')
        pyautogui.keyUp("ctrl")
        print("I can see so refresh")
        time.sleep(0.5)
    else:
        print("not yet")
        time.sleep(0.5)
