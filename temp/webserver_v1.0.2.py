import machine
import network
import socket
import time

# Set up network credentials
ssid = 'm50AF67_TARS'
password = 'D7'

# Initialize and connect to the Wi-Fi network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

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

# Read the HTML file
with open('default.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Set up socket and bind to address
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)

# Listen for connections
s.listen(1)
print('Listening on', addr)

# Handle client connections
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        print(request)

        # Process the request
        request = request.decode()  # Convert bytes to string

        response = html.encode()  # Convert string to bytes

        cl.send(b'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('Connection closed')
