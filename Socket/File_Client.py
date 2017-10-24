# client.py

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
#host = socket.gethostname()     # Get local machine name
host='127.0.0.1'
port = 60004                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('Homework.txt', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('Connection closed')
