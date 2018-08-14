# coding: latin-1
import sys
import os
import time

W = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'
B = '\033[34m'
Y = '\033[33m'
LB = '\033[1;36m'

print Y+"[install]", N+"hit", Y+"enter", N+"to install"
choice = raw_input(G+'>')
if choice == "install" or "INSTALL" or "START" or "start" :
	print R+"[!]", N+"YOU DO NEED THE PYTHON MODULE SOCKS INSTALLED TO RUN FADE.PY"
	print Y+"[~]", N+"HERE I WILL INSTALL IT FOR YOU"
	os.system("pip install requests")
	os.system("pip install requests[socks]")
	time.sleep(4.5)
	os.system("figlet -f mono9 INSTALLING")
	os.system("figlet -f mono9 /UPDATING")
	os.system("figlet -f mono9 PLEASE WAIT")
	os.system("apt-get install lolcat && gem install lolcat")
	os.system("apt-get install tor")

none_ascii = '''
	
  ███████████                   ████████
 ░    ███    ░                 ░ ███    ░
      ███      ███      ███      ██████
      ███     ░ ██      ██ ░     ███   ░
      ███       ██      ██       ███
      ███       ██      ██       ███
     █████       ░██████░       █████
'''
print R+(none_ascii.decode('utf-8'))
time.sleep(1)
print B+"[~]", N+"exiting installer..."
time.sleep(1)
sys.exit()
