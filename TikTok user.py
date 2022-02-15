import requests 
from time import sleep 
import threading 
import uuid 
import sys 
import os 
from random import *
import colorama 
from colorama import *
import time 
import string 
from user_agent import generate_user_agent
import random
import requests, uuid, sys, os
from random import *
import colorama
from colorama import *
import time, string
from user_agent import generate_user_agent
import random, pyfiglet
import webbrowser
h = '_' 
t = '\033[1;36m'
a = '\033[1;32m'
c ='\033[1;32m'
v ='\033[1;31m'
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m' 
q = '\033[2;39m'
o = '\033[2;32m'
y = '\033[1;34m'
b = '\033[2;36m'
z = '\033[1;31m'
x = '\033[1;33m'
r = '\033[0;31m'
P56 = pyfiglet.figlet_format("   D V N I  ")

def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.015)
j(X + P56)
print('      Code By : @dvnishop - @dvniqana ')
rs = requests.Session()
print("---------------------------------")
speed = int(input(''+y+'('+q+'!'+x+')'+y+' ⌯ Choose a speed :'+o))
token = input (''+y+'('+q+'!'+x+')'+y+'  ⌯ Enter Token :  '+o)
ID = input (''+y+'('+q+'!'+x+')'+y+'  ⌯ Enter ID :  '+o)
webbrowser.open('https://t.me/dvniqana')
print("---------------------------------")
input(f"Click Enter To Start \n")
def fg():
	jj9mj = 'poiuytrewqasdfghjklmnbvcxz12'
	gg = '\033[1;31m'
	g = '\033[1;32m'
	All = 0
	Good = 0
	Bad = 0
	while True:
	    user = str("".join(random.choice(jj9mj)for i in range(4)))	    
	    url = f'https://www.tiktok.com/@{user}?lang=ar'
	 #⌯ Ͳele @dvnishop - @dvniqana
	    headers = {
	        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
	        "Connection": "close",
	        "Host": "www.tiktok.com",
	        "Accept-Encoding": "gzip, deflate",
	        "Cache-Control": "max-age=0"
	    }
          #⌯ Ͳele @dvnishop - @dvniqana						
	    re = rs.get(url, headers=headers)
	    if re.status_code == 404:
	        All += 1
	        Good += 1
        	tlg = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= USER Tik Tok : {user}\n⌯ Ͳele @dvni - @dvniqana '
	        req = requests.post(tlg)	
	        print(a+'['+v+f'Y'+a+'] ✅✅ '+c+f'-[{user}]')
	        with open("Don-uaer.txt", "a") as Save:
	            Save.write(f"{user}\n")
	    elif re.status_code == 200:
	        All += 1
	        Bad += 1
	        print(a+'['+v+f'N'+a+']  ❌❌'+v+f'-[{user}]')
#⌯ Ͳele @dvnishop - @dvniqana
	    else:
	        print(a+'['+v+f'M'+a+']  ❌❌'+t+f'-[{user}]')
	        
	the_list.close()
thread = []
for i in range(speed):
	thread1 =threading.Thread(target=fg)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
#⌯ Ͳele @dvnishop - @dvniqana