import pyautogui
import pyperclip
import random
import time
from termcolor import colored
import os

os.system('cls')
print(colored(r"""
	 _______ ____   ____  _       _____ _____        __  __ 
|__   __/ __ \ / __ \| |     / ____|  __ \ /\   |  \/  |
   | | | |  | | |  | | |    | (___ | |__) /  \  | \  / |
   | | | |  | | |  | | |     \___ \|  ___/ /\ \ | |\/| |
   | | | |__| | |__| | |____ ____) | |  / ____ \| |  | |
   |_|  \____/ \____/|______|_____/|_| /_/    \_\_|  |_|
                     created by trantrungkien""", 'red'))
print(colored("\n===========================================\n", 'green'))

msg = input("nhap noi dung spam: ").split(" ll ")
n = int(input("nhap so lan spam: "))
m = float(input("nhap thoi gian ngung: "))

os.system('cls')
print(colored(r"""
	 _____  _           __     _______ _____        __  __ 
|  __ \| |        /\\ \   / / ____|  __ \ /\   |  \/  |
| |__) | |       /  \\ \_/ / (___ | |__) /  \  | \  / |
|  ___/| |      / /\ \\   / \___ \|  ___/ /\ \ | |\/| |
| |    | |____ / ____ \| |  ____) | |  / ____ \| |  | |
|_|    |______/_/    \_\_| |_____/|_| /_/    \_\_|  |_| """,'green'))
print(colored("\n=====================================================",'red'))

time.sleep(2)
print(colored("\n[+] Strat......",'green'))
time.sleep(1)
print(colored("\n3",'green'))
time.sleep(1)
print(colored("\n2",'green'))
time.sleep(1)
print(colored("\n1",'green'))
time.sleep(1)

for i in range(n):
	pyperclip.copy(random.choice(msg))
	pyautogui.hotkey("ctrl","V")
	pyautogui.press("enter")
	time.sleep(m)