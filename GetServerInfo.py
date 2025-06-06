import dns.resolver
import os
import time

server = input("Enter srever: ")

def dns_resolver_resolve(hostname):
    try:
        answers = dns.resolver.resolve(hostname, 'A')
        for rdata in answers:
            print(f"IP Address: {rdata}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {hostname} not found.")
    except dns.resolver.NoAnswer:
        print(f"No answer for {hostname}.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Scaning server...")
time.sleep(2)
os.system("clear")

print("Serever Results: ")
print("--------------------------------------------------")

dns_resolver_resolve(server)

time.sleep(2)
print("\n")
mainmenu = input("Do you want to go back to the main menu? (Y/N) ")
if mainmenu == "Y":
    subprocess.run(["python", "TheRedGlaer.py"])
elif mainmenu == "n":
    os.system("clear")
    os.system("exit")
else:
    print("That's not a option")
    time.sleep(2)
    os.system("exit")
