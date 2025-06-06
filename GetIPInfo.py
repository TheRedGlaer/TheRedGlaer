import webbrowser
import time
import subprocess
import os

print("Copy this command and paste it in the terminal: curl http://ipinfo.io/theip/")
time.sleep(3)
print("Where it says theip change it with a real ip for example: (143.xxx.xxx.xx, 143.xxx.x.xx)")
time.sleep(3)
print("For example your IP info")
time.sleep(2)
print("Your IP info is: ")
print("-----------------------------------------")
time.sleep(2)
subprocess.run(["curl", "http://ipinfo.io/"])
print(" ")
time.sleep(3)
print("The its gonna print the results in the terminal")
time.sleep(2)
print("That all enyoj!")
time.sleep(3)
mainmenu = input("Do you want to go to the menu? (Y/N) ")
if mainmenu == "y":
    subprocess.run(["python", "TheRedGlaer.py"])
elif mainmenu == "n":
    os.system("clear")
    time.sleep(3)
    os.system("exit")
time.sleep(2)
