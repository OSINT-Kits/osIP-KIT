# IMPORTS
import os
import socket as s
import sys
import json
import urllib
from urllib.request import urlopen
import time
import requests
from scapy import *
from pyfiglet import figlet_format
from colorama import Fore, Style
# MENU
print (Style.BRIGHT + Fore.GREEN +"                 W E L - C O M E ")
time.sleep(0.5)
print (figlet_format("osIP-Kit", font = "slant"))
print ("==================================")
print ("Made By Ahmad")
print ("Replit: @AhmadTheWeirdo")
print ("YouTube: Black Magic") 
print ("==================================")
time.sleep(0.5)
# VARIABLES
choice = input("[*] ")
ping = ""
ipflood = ""
# COMMANDS
def ask():
  choice = input("[*] ")
if choice == "ping":
    os.system("python p.py")
    ask()
elif choice == "ipflood":
     os.system("d.py")
elif choice == "nmap":
	os.system("python n.py")
	ask()	
elif choice == "help":
	print ("""
	----------------------------------------------------------
	clear -- clears the screen
	ipflood -- spam http requests to an ip
	nmap -- nmap the ip and shows the open ports
	iplookup -- shows the info of the ip/your ip
	macflood -- floods the mac address with requests
	ncat -- makes a reverse shell script
	install -- installs all the requirements
	credits -- prints who made the script
	---------------------------------------------------------
	""")
	ask()
elif choice == "credits":
	print ("""
	Made By Ahmad
	Made For Educational Purposes Only/ Penetration Testing
	""")
	ask()
elif choice == "install":
	print ("[*] Installing...")
	done = False
	os.system("sudo apt-get nmap netcat && sudo pip3 install scapy")
	ask()
	if done == True:
		print ("[*] Restarting Device...")
		os.system("sudo reboot")
		ask()
elif choice == "iplookup":
	os.system("bash ii.sh")
	ask()
elif choice == "macflood":
	os.system("python mf.py")
	ask()
elif choice == "ncat":
	os.system("python nc.py")
	ask()
elif choice == "clear":
	if os.name=="nt":
		os.system("cls")
		ask()
	else:
		os.system("clear")
		ask()
