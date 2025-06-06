import socket
import threading
import subprocess
import os
import time


def scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print("Port", port, "is open")
        sock.close()
    except Exception as e:
        print("Port", port, "is closed")

host = input("Enter IP: ")
ports = list(range(1, 1000))

print("Starting scan...")
time.sleep(2)
print("Scaning Ports...")
time.sleep(2)
os.system("clear")
print("Ports: ")
print("----------------------------------------------------")


threads = []
for port in ports:
    thread = threading.Thread(target=scan, args=(host, port))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


returntomenu = input("Do you want to scan again? (Y/N) ")
if returntomenu == "y":
     subprocess.run(["python", "ScanPorts.py"])
else:
     subprocess.run(["python", "TheRedGlaer.py"])
