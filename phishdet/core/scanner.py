# Coded by HS Devansh Raghav
# A tool by Whoamisec
import re
import requests
import json
import sys
import socket
import ipwhois
import threading
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from phishdet.db.db import directories_db
from phishdet.core.colors import good, bad, info, bright, cyan, reset, red, green, warn, res, err
from phishdet.db.db import black_list
import time
Passed = 0
Failed = 0
dirs = []
found_keywords = []
found_keywords2 = []
found_keywords3 = []
login_keywords = ['Signout','Signin','Signup','sign in','Sign In','Sign in', 'SIGN IN', 'SIGN UP' , 'sign up', 'Sign Up' , 'Sign up', 'Register', 'REGISTER', 'register' , 'Forgot Password?', 'password', 'Password', 'Log in', 'Login', 'log in', 'Log In', 'LOG IN', 'Login ID', 'username', 'Username', 'SIGN OUT' , 'sign out' ,'Sign out', 'Sign Out']

def inf(target):
    print('\n'+info + 'Retrieving some basic information about target...'+'\n')
    sleep(2)
    if re.search('https://', target):
        target2 = target.replace('https://', '')
    elif re.search('http://', target):
        target2 = target.replace('http://', '')
    else:
        target2 = target
    try:
        print(res + 'Target : ' + target)
        ip = socket.gethostbyname(target2)
        print(res + 'IP address : ' + ip)
        req = requests.get(target)
        server = req.headers['Server']
        print(res + 'Server : ' + server)
    except Exception:
        print(err + 'Unexpected error occured!')


def scan(target):
    global Passed
    global Failed
    print('\n'+info + 'Analysing Specified URL...' + '\n')
    sleep(2)
    req = requests.get(target)
    resp2 = req.url

    if re.findall('http://', resp2):
        Failed += 1
        print(bad + 'The website is not using SSL, this may allow attackers to steal your credentials')

    if re.findall('https://', resp2):
        Passed += 1
        print(good + 'The website is using SSL (Secure Sockets Layer)')

    if re.findall('ngrok', target):
        Failed += 1
        print(bad + '"ngrok" keyword is detected in the URL, this may be a Phishing link')


def whois(target):
    global Passed
    global Failed
    print('\n' + info + 'Performing a Whois Lookup, this can be used to identify Phishing links...'+'\n')
    sleep(2)
    if re.search('https://', target):
        target = target.replace('https://', '')
    elif re.search('http://', target):
        target = target.replace('http://', '')
    else:
        target = target

    ip = socket.gethostbyname(target)

    try:
        lookup = ipwhois.IPWhois(ip)
        result = lookup.lookup_whois()

        for key, value in result.items():
            if value != None:
                if isinstance(value, list):
                    for item in value:
                        for key, value in item.items():
                            if value != None:
                                print(res+bright + cyan + '{}:'.format(str(key)) + reset, str(
                                    value).replace(',', ' ').replace('\r', ' ').replace('\n', ' '))
                            else:
                                pass
                else:
                    print(res+bright + cyan + '{}:'.format(str(key)) + reset,
                          str(value).replace(',', ' ').replace('\r', ' ').replace('\n', ' '))

            else:
                pass
    except:
        Failed += 1
        print(bad + 'No data found!')


def scan2(target):
    global Passed
    global Failed
    print('\n'+info + 'Searching Browsers Phishing Warning Keywords in the response...'+'\n')
    sleep(2)
    send_req = requests.get(target)
    rep = send_req.content
    rep = rep.decode('ISO-8859-1')

    def runner(keyword):
        if re.findall(keyword, rep):
            found_keywords.append(keyword)
            print(bad + f'{bright}{cyan}"{keyword}"{reset} is detected in the response')
        else:
            print(good + bright + f'"{keyword}"' + reset, 'not found in the response')
    with ThreadPoolExecutor(max_workers=40) as executor:
        for keyword in black_list:
            executor.submit(runner, keyword)

    if len(found_keywords) == 0:
        Passed += 1
    else:
        Failed += 1

def port_scanner(target):
    print('\n' + info + 'Scanning ports, check if any unexpected or vulnerable port is open...')
    sleep(2)
    if re.search('https://', target):
        target = target.replace('https://', '')
    elif re.search('http://', target):
        target = target.replace('http://', '')
    print_lock = threading.Lock()
    port_range = input(
        '\n' + bright + "Scan up to port (example would be 1000): " + reset)
    print('')

    def scan(target, port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)

        try:
            scanner.connect((target, port))
            service = socket.getservbyport(port, 'tcp')
            scanner.close()

            with print_lock:
                print(res + 'OPEN:', port, service)
        except:
            pass

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(int(port_range)):
            executor.submit(scan, target, port + 1)

def ds(target):
    print('\n' + info + 'Searching for directories and files on the target website, most of the websites contains other files and directories to provide some data or functionalities to the users so if this tools finds no directory or file then it will automatically run a login page keyword scan to conform if it is a phishing page...' + '\n')
    sleep(2)
    if target.endswith('/'):
        print(err + 'The target ends with "/", Please try again without adding "/" at the end :)')
        quit()
    else:
        pass

    def search(target, dir):
        try:
            build_url = (target + '/' + dir)
            req = requests.get(build_url)
            resp = req.status_code

            if resp == 200:
                print(res + 'Found : ' + build_url)
                dirs.append(build_url)
                
        except KeyboardInterrupt:
            quit()
        except requests.exceptions.ConnectionError:
            print(err + 'requests.exceptions.ConnectionError:', build_url)

    with ThreadPoolExecutor(max_workers=100) as executor:
        for dir in directories_db:
            executor.submit(search,target,dir)

def scan3(target):
    global Passed
    global Failed
    if (len(dirs)) == 0:
        print('\n'+warn + 'Not a single directory found on the target, this may be a phishing page.')
        print('\n'+info + 'Checking if there is any login page keywords to conform that it is a phishing page...' + '\n')
        send_req = requests.get(target)
        rep = send_req.content
        rep = rep.decode('ISO-8859-1')

        for keyword in login_keywords:
            if re.findall(keyword, rep):
                found_keywords2.append(keyword)
                print(bad + f'{bright}{cyan}"{keyword}"{reset} is detected in the response')
            else:
                print(good + bright + f'"{keyword}"' +reset, 'not found in the response')
            if len(found_keywords2) == 0:
                Passed += 1
            else:
                Failed += 1
    else:
        Passed += 1
        print(good, len(dirs), 'directories found on the target')

def find_login_page(target,loginS):
    if loginS == True:
        global Passed
        global Failed
        print('\n'+info + 'Checking if there is any login page keywords...' + '\n')
        sleep(2)
        send_req = requests.get(target)
        rep = send_req.content
        rep = rep.decode('ISO-8859-1')

        for keyword in login_keywords:
            if re.findall(keyword, rep):
                found_keywords3.append(keyword)
                print(warn + f'{bright}{red}"{keyword}"{reset} is detected in the response')
            else:
                print(good + bright + f'"{keyword}"' +reset, 'not found in the response')
        if len(found_keywords3) == 0:
            Passed += 1
        else:
            Failed += 1 
    else:
        pass

def exe(target, loginS):
    inf(target)
    scan(target)
    scan2(target)
    whois(target)
    port_scanner(target)
    ds(target)
    scan3(target)
    find_login_page(target, loginS)

    print('\n'+green + bright+ 'Result : ' + reset)
    print('Test Passed:', Passed)
    print('Test Failed:', Failed)
