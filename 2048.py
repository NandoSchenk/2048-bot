#!/bin/python

import pyautogui
import time
import random
import os
import keyboard

arrow = ['w', 'a', 's', 'd']
text = ''


def randString():  # generates random String with wasd
    text = ''
    for i in range(200):
        text += arrow[random.randint(0, 3)]
    return text


def play():  # writes the random String
    pyautogui.write(randString())


def isOnTryAgain():  # Clicks, to restart game
    pyautogui.click()


def go():  # Puts everything with some text together
    os.system('clear')
    print('Open 2048 with Mouse on Try again button')
    print('')
    time.sleep(.5)
    for i in range(5, 0, -1):  # Countdown
        print(i)
        time.sleep(1)
    print('')
    time.sleep(.5)
    print('Go!')
    print('')
    print('hold "r" to stop')
    while not keyboard.is_pressed('r'):
        randString()
        play()
        isOnTryAgain()


try:  # Check if program has sudo rights
    keyboard.is_pressed("r")
    go()
except:
    print('You have to be admin (for the keyboard library)')
