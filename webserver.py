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
import sys
import os
import uos
#import select


      
def main_program():
    # Add your main program logic here
    print("Running main program...")
    
#load the program till to read the lasat else 
    
    
    
# This is going to help the usage of machine.restet()

'''

    By adding this check, the machine.reset() command
    will only be executed if the script is being run as
    the main program, i.e., directly executed by Thonny.

'''
'''
if __name__ == '__main__':
    # Reset the Raspberry Pi Pico to ensure a clean start
    machine.reset()# Check if running as main program
'''


#---------
# Initialize and connect to the Wi-Fi network
# Casa
'''
ssid = 'movisF67_TARS'
password = 'gpbxD7'
'''

# Depto
ssid = 'movF185DF'
password = '~6qp'

#---------

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
#-------------------------
# It's recommendable to insert a full webpage in a iframe, as in the default.html file has
'''
with open('default.html', 'r', encoding='utf-8') as f:
    html = f.read()
'''

#-------------------------
# Read the HTML file
#-------------------------
# It's recommendable to insert a full webpage in a iframe, as in the default.html file has
'''
with open('default.html', 'r', encoding='utf-8') as f:
    html = f.read()
'''

# Get the directory path of the script
script_dir = uos.getcwd()

# Specify the HTML file to load
html_file = 'default.html'

# Construct the file path
file_path = script_dir + '/' + html_file

# Initialize HTML content variable
html = ''

try:
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
except OSError:
    print(f"File not found: {file_path}")
else:
    print(f"Loaded HTML file: {file_path}")

# Option 1: If the specified file is not found, load a default HTML file
if not html:
    default_path = script_dir + '/default.html'
    try:
        with open(default_path, 'r', encoding='utf-8') as f:
            html = f.read()
    except OSError:
        print(f"Default HTML file not found: {default_path}")
    else:
        print(f"Loaded default HTML file: {default_path}")

# Option 2: If both the specified file and default file are not found, display an error message
if not html:
    print("HTML file not found. Please ensure the file exists in the specified location.")



#-------------------------


'''
# Set up socket and bind to address v1.0

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
'''

# Set up socket and bind to address
# V2.0: in a while we avoid any possible error if there's any other port open

# ---------
 

port = 80
while True:
    try:
        addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
        s = socket.socket()
        '''
        TO AVOID THIS ERROR: OSError: [Errno 98] EADDRINUSEOSError: [Errno 98] EADDRINUSE
        PREVIOUSLY only way to fix it is running this COMMAND in the console:
            machine.reset()
        '''
        # I'VE ADDED THE NEXT LINE: 
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Enable reusing the address
        s.bind(addr)
        break
    except OSError as e:
        if e.args[0] == 98:  # Address already in use
            print(f"Port {port} is already in use, trying a different port...")
            port += 1
        else:
            raise e
        
# Set socket to non-blocking
# s.setblocking(False)

# Listen for connections
s.listen(1)
print('Listening on', addr)

# Set socket timeout to handle unresponsive connections
'''
 I've added the line s.settimeout(5) to set a timeout
 of 5 seconds for socket operations. This means that if
 a client connection is unresponsive for more than 5 seconds,
 a socket.timeout exception will be raised, allowing the server
 to continue running and accept new connections.
'''
# s.settimeout(5)  # 5 seconds timeout (adjust as needed)

# Handle client connections
try:
    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = b''

        # Receive the request in chunks until the complete request is received
        while b'\r\n\r\n' not in request:
            chunk = cl.recv(1024)
            if not chunk:
                break
            request += chunk

        if not request:
            print('Empty request, closing connection')
            cl.close()
            continue

        # Convert the request bytes to string
        request = request.decode()

        # Extract the HTTP method and path from the request
        method, path, _ = request.split(' ', 2)

        print('Request:', method, path)

        # Process the request based on the path
        if path == '/':
            response = html.encode()
            content_type = 'text/html'
        else:
            # Handle other paths or return a 404 Not Found
            response = b'404 Not Found'
            content_type = 'text/plain'

        # Send the HTTP response headers
        response_headers = f'HTTP/1.0 200 OK\r\nContent-type: {content_type}\r\n\r\n'
        cl.send(response_headers.encode())

        # Send the response content
        cl.send(response)

        # Close the connection after sending the response
        cl.close()
        print('Connection closed')

except KeyboardInterrupt:
    print('Keyboard interrupt detected, shutting down...')

finally:
    # Close the socket
    s.close()
    


#-------------------------


'''
# Set up socket and bind to address v1.0

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
'''

# Set up socket and bind to address
# V2.0: in a while we avoid any possible error if there's any other port open

# ---------
 

port = 80
while True:
    try:
        addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
        s = socket.socket()
        '''
        TO AVOID THIS ERROR: OSError: [Errno 98] EADDRINUSEOSError: [Errno 98] EADDRINUSE
        PREVIOUSLY only way to fix it is running this COMMAND in the console:
            machine.reset()
        '''
        # I'VE ADDED THE NEXT LINE: 
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Enable reusing the address
        s.bind(addr)
        break
    except OSError as e:
        if e.args[0] == 98:  # Address already in use
            print(f"Port {port} is already in use, trying a different port...")
            port += 1
        else:
            raise e
        
# Set socket to non-blocking
# s.setblocking(False)

# Listen for connections
s.listen(1)
print('Listening on', addr)

# Set socket timeout to handle unresponsive connections
'''
 I've added the line s.settimeout(5) to set a timeout
 of 5 seconds for socket operations. This means that if
 a client connection is unresponsive for more than 5 seconds,
 a socket.timeout exception will be raised, allowing the server
 to continue running and accept new connections.
'''
# s.settimeout(5)  # 5 seconds timeout (adjust as needed)



# Handle client connections
try:
    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = b''

        # Receive the request in chunks until the complete request is received
        while b'\r\n\r\n' not in request:
            chunk = cl.recv(1024)
            if not chunk:
                break
            request += chunk

        if not request:
            print('Empty request, closing connection')
            cl.close()
            continue


            request = client_info["request"]
            print("Received request:", request)
            response = "Server received: " + request
            client_info["socket"].send(response.encode())

            # Log client information
            log_message = f"Client: {client_info['address']} - Request: {request}"
            print(log_message)
            with open("server.log", "a") as log_file:
                log_file.write(log_message + "\n")
                



        # Convert the request bytes to string
        request = request.decode()

        # Extract the HTTP method and path from the request
        method, path, _ = request.split(' ', 2)

        print('Request:', method, path)

        # Process the request based on the path
        if path == '/':
            response = html.encode()
            content_type = 'text/html'
        else:
            # Handle other paths or return a 404 Not Found
            response = b'404 Not Found'
            content_type = 'text/plain'

        # Send the HTTP response headers
        response_headers = f'HTTP/1.0 200 OK\r\nContent-type: {content_type}\r\n\r\n'
        cl.send(response_headers.encode())

        # Send the response content
        cl.send(response)

        # Close the connection after sending the response
        cl.close()
        print('Connection closed')

except KeyboardInterrupt:
    print('Keyboard interrupt detected, shutting down...')
    

finally:
    # Close the socket
    s.close()
    
    
#  executed the code on power unless is connected via thonny
# Define the USB power detection pin
usb_power_pin = machine.Pin(6, machine.Pin.IN)

# Check if the program is running on USB power
if usb_power_pin.value() == 1:
    # Run the program immediately
    print("Running program on USB power...")
    main_program()

else:
    # Wait until the program is executed via Thonny
    print("Waiting for program execution via Thonny...")
    while usb_power_pin.value() == 0:
        time.sleep(1)

    # Run the program after it is executed via Thonny
    print("Running program after Thonny execution...")
    main_program()
    
    

