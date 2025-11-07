# get data 
from pyfiglet import Figlet
import re
from ping3 import ping
import random as rd
from termcolor import colored

def is_valid_host(host):
    # Basic check for IP or domain format
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    domain_pattern = r'^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    return re.match(ip_pattern, host) or re.match(domain_pattern, host)


def ping_data():
    lstext = ["I break firewalls, not promises","Hack the planet","Trust no one","I see through the matrix","Code is my weapon. Silence is my shield","Freedom is choice","Silence speaks","Change is constant","Know yourself"]
    lscolor = ["red","green","white","blue","magenta","cyan","yellow"]
    text = Figlet(font="slant")
    codecolor = text.renderText(f"{rd.choice(lstext)}")
    print(colored(text=codecolor,color=f"{rd.choice(lscolor)}",attrs=["dark", "blink","bold"],))
    getentrie = input("Please insert hosts you want to check, separated by commas: ")
    hosts = [h.strip() for h in getentrie.split(",") if h.strip()]

    if not hosts:
        print("You didn't insert anything 🤨")
    else:
        print("\n========== Ping Results ========== \n")
        for host in hosts:
            if not is_valid_host(host):
                print(f"{host} is not a valid hostname or IP address.")
                continue
            try:
                result = ping(host, timeout=1)
                if result is not None:
                    print(f"{host} is reachable: {result * 1000:.2f} ms")
                else:
                    print(f"{host} is unreachable.")
            except Exception as e:
                print(f"Error pinging {host}: {e}")



if __name__ == "__main__":
    ping_data()