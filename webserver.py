'''
********************************************
SMALL WEB SERVER FOR RASPBERRY PI PICO W 2
USING MICROPYTHON WITH THONNY IDE
********************************************
BY ENGINEER: FELIPE ALFONSO GONZALEZ L.
EMAIL: F.ALFONSO@RES-EAR.CH
********************************************
LICENCE : MIT & GNU/GPL
---------------------------------
---------------------------------

INSERT THIS IN THE THONNY'S CONSOLE IDE
IF THERE IS ANY ERROR CONNECTING:
---------------------------------
machine.reset()
---------------------------------

'''

import machine
import network
import socket
import time


ssid = 'wifi-name'
password = 'password'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

#loading the html file

with open('default.html', 'r', encoding='utf-8') as f:
    html = f.read()


max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()

# 
'''
next line - s.bind(addr) -, generates this error:
Traceback (most recent call last):
  File "<stdin>", line 60, in <module>
OSError: [Errno 98] EADDRINUSE

--
only way to fix it is running this lines in the console:
machine.reset()

'''

s.bind(addr)

#-----------

s.listen(1)

print('listening on', addr)

#  Listen for connections

while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)

        request = str(request)
#
        response = html
# encode()

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        #there's an error in the line below 
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')


    

