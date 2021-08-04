import os

done = False
ip = input ("[*] Enter IP Address: ")
done = True
if done == True:
	os.system("nmap "+ip)