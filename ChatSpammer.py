# -*- coding: utf-8 -*-
'''
A full fledged chat spamming tool.

@author: Mr. Shark Spam Bot
'''
import time
import sys
import pyautogui
import pyperclip

# Define variables needed.
MESSAGE_PRINT = 'Please enter your message.'
NUMBER_PRINT = 'Please enter the number of times you want your message to be sent.'
XY_PRINT = 'Please enter the x y coordinates of where your message should be typed.(ex: 1200 320)'
SEC_PRINT = 'Please enter the number of seconds you want to leave for yourself to open the chat.'
X_PRINT = 'Please enter the x coordinate of where your message should be typed.'
Y_PRINT = 'Please enter the y coordinate of where your message should be typed.'
VALID_PRINT = '(make sure it is valid!!!)'

# Print everything needed to user and get info needed to spam.
try:

    print('''
\t░█████╗░██╗░░██╗░█████╗░████████╗
\t██╔══██╗██║░░██║██╔══██╗╚══██╔══╝
\t██║░░╚═╝███████║███████║░░░██║░░░
\t██║░░██╗██╔══██║██╔══██║░░░██║░░░
\t╚█████╔╝██║░░██║██║░░██║░░░██║░░░
\t░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░

\t░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
\t██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
\t╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
\t░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
\t██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
\t╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
\tCreated by Mr. Shark Spam Bot.
    ''')
    print(MESSAGE_PRINT)
    spam_message = input('> ')
    print(NUMBER_PRINT)
    sending_number = input('> ')
    print(XY_PRINT)
    coordinates = input('> ')
    print(SEC_PRINT)
    opening_time = input('> ')

    # Check for valid input.
    while True:
        spam_message = spam_message.strip()
        if spam_message:
            break
        print(MESSAGE_PRINT + '(make sure you type something in!!!)')
        spam_message = input('> ')

    while True:
        sending_number = sending_number.strip()
        if sending_number.isdecimal():
            break
        print(NUMBER_PRINT + VALID_PRINT)
        sending_number = input('> ')

    coordinates = coordinates.split()
    while True:
        if len(coordinates) == 2:
            x, y = coordinates[0], coordinates[1]
            break
        print(XY_PRINT + VALID_PRINT)
        coordinates = input('> ')
        coordinates = coordinates.split()

    while True:
        if x.isdecimal() and y.isdecimal():
            if int(x) <= pyautogui.size()[0] and int(y) <= pyautogui.size()[1]:
                break
            if not int(x) <= pyautogui.size()[0]:
                print(X_PRINT + VALID_PRINT)
                x = input('> ')
            if not int(y) <= pyautogui.size()[1]:
                print(Y_PRINT + VALID_PRINT)
                y = input('> ')
        if not x.isdecimal():
            print(X_PRINT + VALID_PRINT)
            x = input('> ')
        if not y.isdecimal():
            print(Y_PRINT + VALID_PRINT)
            y = input('> ')

    while True:
        opening_time = opening_time.strip()
        if opening_time.isdecimal():
            break
        print(SEC_PRINT + VALID_PRINT)
        opening_time = input('> ')

    # Tell user to switch screen.
    opening_time = int(opening_time)
    for i in range(opening_time):
        print('\rYou have %i seconds to open the chat in a browser...' % opening_time, end='')
        time.sleep(1)
        opening_time -= 1

    # Move to screen coordinates and start spamming.
    try:
        pyperclip.copy(spam_message)
        sending_number = int(sending_number)
        pyautogui.click(int(x), int(y))
        pyautogui.PAUSE = 0
        for i in range(sending_number):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
        print('\n\n[+] Possibly sent "%s" %i times.' %
              (spam_message, sending_number))
    except pyautogui.FailSafeException:
        print('\n\n[+] Fail safe triggered.')
        print('[-] Terminating program.')
        sys.exit()

except KeyboardInterrupt:
    print('\n[+] Ctrl + c detected.')
    print('[-] Terminating program.')
    sys.exit()
