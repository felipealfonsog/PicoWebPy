'''
********************************************
SMALL WEB SERVER FOR RASPBERRY PI PICO W 2
USING MICROPYTHON WITH THONNY IDE
********************************************
BY ENGINEER: FELIPE ALFONSO GONZALEZ L.
EMAIL: F.ALFONSO@RES-EAR.CH
********************************************
LICENCE : MIT & GNU/GPL
--------------------------------------------

'''

import machine
import network
import socket
import time


    
#---------
# Initialize and connect to the Wi-Fi network
ssid = '----wifi-id---'
password = '---pwd----'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

'''
#loading the html file
V.1.0: 
with open('default.html', 'r', encoding='utf-8') as f:
    html = f.read()
'''


# Wait for the network connection
# Loading the html file
# It's recommendable to insert a full webpage in a iframe, as in the default.html file has

# Wait for the network connection
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('Network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print('IP:', status[0])

#-------------------------
# Read the HTML file
# It's recommendable to insert a full webpage in a iframe, as in the default.html file has
with open('default.html', 'r', encoding='utf-8') as f:
    html = f.read()
#-------------------------


'''
# Set up socket and bind to address v1.0

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
'''

# Set up socket and bind to address
# V2.0: in a while we avoid any possible error if there's any other port open
port = 80
while True:
    try:
        addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
        s = socket.socket()
        s.bind(addr)
        break
    except OSError as e:
        if e.args[0] == 98:  # Address already in use
            print(f"Port {port} is already in use, trying a different port...")
            port += 1
        else:
            raise e

# Listen for connections
s.listen(1)
print('Listening on', addr)

# ---------
'''
next line - s.bind(addr) -, generates this error:
Traceback (most recent call last):
  File "<stdin>", line 60, in <module>
OSError: [Errno 98] EADDRINUSE

--
only way to fix it is running this lines in the console:
machine.reset()

'''

'''
s.bind(addr)


s.listen(1)

print('listening on', addr)
'''

'''
V.1.0 Code:

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

'''

# Handle client connections
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        print(request)

        # Process the request
        # Request = str(request) (old implementation)
        request = request.decode()  # Convert bytes to string

        response = html.encode()  # Convert string to bytes
        # encode()

        cl.send(b'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        # There's an error in the line below  (Fixed using encode() & deode() )
        cl.send(response)
        cl.close()

# Add more exceptions as errors apart from the one below 
    except OSError as e:
        cl.close()
        print('Connection closed')

        #KeyboardInterrupt exception
        '''
        except KeyboardInterrupt as addr:
        machine.reset()
        '''

                
# Check if running as main program
# This is going to help the usage of machine.restet()

'''

    By adding this check, the machine.reset() command
    will only be executed if the script is being run as
    the main program, i.e., directly executed by Thonny.

'''

 
if __name__ == '__main__':
            # Reset the Raspberry Pi Pico to ensure a clean start
        machine.reset()
         

