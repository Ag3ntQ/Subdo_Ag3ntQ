import requests
import socket as s
import os
from threading import Thread


def subdomain():
    print(Y)
    os.system(f"figlet SubdoBrute")
    space = 10 * " "
    print(f"{C}{space}https://github.com/Ag3ntQ{W}\n")
    subdomains = open("subdomains.txt", 'r').read().splitlines()
    thread = 40  # it can be changed to
    diff = int(len(subdomains) / thread)
    i = 0  # start index
    for j in range(diff, len(subdomains) + 1, diff):
        t = Thread(target=subdomain_helper, args=(subdomains[i:j],))
        t.start()
        i = j
    # to lefter lines in wordlist
    if j != len(subdomains):
        t = Thread(target=subdomain_helper, args=(subdomains[i: len(subdomains)],))
        t.start()


def subdomain_helper(subdomains):
    for sub_domain in subdomains:
        url = f'{sub_domain}.{target}'
        try:
            get_url = "http://" + url
            res = requests.get(get_url, headers=head)
            if res.status_code != 404:
                iip = s.gethostbyname(url)
                print(f"{G}[•] {url} [{iip}]{W}")
        except requests.ConnectionError:
            # doesn't print error to make output more beauty
            pass


if __name__ == '__main__':
    # variables that to be used globally
    G = "\033[32m"  # Green
    W = "\033[0m"  # White
    R = "\033[31m"  # Red
    C = "\033[36m"  # Cyan
    B = "\033[34m"  # Blue
    Y = "\033[33m"  # Yellow
    user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 " \
           "Safari/537.36 "
    head = {"User-Agent": user}
    target = input(f"{B}\n[#] Enter Domain : {W}")
    subdomain()
