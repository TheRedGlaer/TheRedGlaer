import os
import socket
import time
import threading
import subprocess
from colorama import Fore, Style, Back

time.sleep(3)

def options():
    time.sleep(2)
    logo = Fore.RED + '''
  ▄▄▄█████▓██░ ██▓█████     ██▀███ ▓█████▓█████▄      ▄████ ██▓   ▄▄▄     ▓█████ ██▀███  
  ▓  ██▒ ▓▓██░ ██▓█   ▀    ▓██ ▒ ██▓█   ▀▒██▀ ██▌    ██▒ ▀█▓██▒  ▒████▄   ▓█   ▀▓██ ▒ ██▒
  ▒ ▓██░ ▒▒██▀▀██▒███      ▓██ ░▄█ ▒███  ░██   █▌   ▒██░▄▄▄▒██░  ▒██  ▀█▄ ▒███  ▓██ ░▄█ ▒
  ░ ▓██▓ ░░▓█ ░██▒▓█  ▄    ▒██▀▀█▄ ▒▓█  ▄░▓█▄   ▌   ░▓█  ██▒██░  ░██▄▄▄▄██▒▓█  ▄▒██▀▀█▄  
    ▒██▒ ░░▓█▒░██░▒████▒   ░██▓ ▒██░▒████░▒████▓    ░▒▓███▀░██████▓█   ▓██░▒████░██▓ ▒██▒
  ▒ ░░   ▒ ░░▒░░░ ▒░ ░   ░ ▒▓ ░▒▓░░ ▒░ ░▒▒▓  ▒     ░▒   ▒░ ▒░▓  ▒▒   ▓▒█░░ ▒░ ░ ▒▓ ░▒▓░
    ░    ▒ ░▒░ ░░ ░  ░     ░▒ ░ ▒░░ ░  ░░ ▒  ▒      ░   ░░ ░ ▒  ░▒   ▒▒ ░░ ░  ░ ░▒ ░ ▒░
  ░      ░  ░░ ░  ░        ░░   ░   ░   ░ ░  ░    ░ ░   ░  ░ ░   ░   ▒     ░    ░░   ░ 
         ░  ░  ░  ░  ░      ░       ░  ░  ░             ░    ░  ░    ░  ░  ░  ░  ░   

    '''

    print(logo)
    time.sleep(2)
    print("1. Scan IP for open ports")
    print("2. Get info from server")
    print("3. Get info from IP Address")
    print("4. DDoS Attack")
    print("-----------------------------------------------------------")
    option = input("Enter option: ")

    if option == "1":
         subprocess.run(["python", "ScanPorts.py"])

    if option == "2":
         subprocess.run(["python", "GetServerInfo.py"])
    if option == "3":
         subprocess.run(["python", "GetIPInfo.py"])
    if option == "4":
         subprocess.run(["python", "DoS.py"])

os.system("clear")
options()
