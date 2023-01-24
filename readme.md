# Elderflower v1.0.3
## HTTP(S) bruteforcing tool

<p>Elderflower is a http bruteforcing tool. It can be used to bruteforce basic http authentication.Have fun with it and you all know, for educational purpose only ;)
<br>Good luck!</p>
### How to install
Upload the script to your server, adapt the code and run it with python3.




### How to use

#### Usage
##### [Server](server.py)
``` bash
python3 server.py -p [port] -f [file] -v (verbose mode)
```
[file] = file with used passwords
Exapmle:
```bash
python3 server.py -p 4545 -f usedpws.txt -v
```
\
##### [Elderflower](elderflower.py)
``` bash 
python3 elderflower.py -u [url] -t [username] -s [server] -p [port] -v (verbose mode) 
```
[url] = url of the target
[username] = username to bruteforce
[server] = ip of the server
Exapmle:
``` bash 
python3 elderflower.py -u http://example.com -t JohnDoe -s https://server.com -P 4545 -v
```
\
#### Addapt the code

##### [bin](bin.py)
The Log files are defined in line 16 & 17.
```python
16  pwLog = 'elderflower.log'               # the found password will be logged here
17  errorLog = 'error.log'                  # errors will be logged here
```

The trigger for the successfull login is defined in line 18.
```python
18  trigger = 'example'                 # trigger for successfull login
```


The payload for the post request is defined in line 24.
```python 
24  payload = {'do':'login', 'user':f'{username}', 'pw':f'{password}'}      # payload for request
```

Passwords are being generated in line 45.
In my case the paswords are 6 characters long. The first character is a random uppercase letter, the next 3 characters are random lowercase letters and the last 2 characters are random digits.

```python
45  def randPW():
46      a = random.choice(uppercase)
47      b = ''.join(random.choice(lowercase) for x in range(3))
48      c = ''.join(random.choice(digits) for x in range(2))
49  
50      password = a+b+c
51      return password
```

