# scripted by @n4zgu1
# elderflower.py v1.0.3

import bin as ef
import getopt
import sys



argv = sys.argv[1:]

if(len(sys.argv) < 5):
    print('Usage: python elderflower.py -u [url] -t [username] -s [server] -p [port] -v (verbose mode)')
    exit()
    
opts, args = getopt.getopt(argv, 'u:t:s:p:v')
for opt, arg in opts:
    if opt in ['-u']:
        url = arg
    if opt in ['-t']:
        target = arg
    if opt in ['-s']:
        host = arg
    if opt in ['-p']:
        port = int(arg)
    if opt in ['-v']:
        verbose = True
    else: verbose = False
    
ef.elderflower(url, target, host, port, verbose)
