import socket

# take the server name and port name

host = 'local host'
port = 5000

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

# connect it to server and port 
# number on local computer.
s.connect(('127.0.0.1', port))

# receive message string from
# server, at a time 1024 B
msg = s.recv(1024)

encrypt = ''
# repeat as long as message
# string are not empty
while msg:
    print('Received:' + msg.decode())
    encrypt += str(msg.decode())
    msg = s.recv(1024)

decrypt = ''
shift = 3
for char in encrypt:
    if(char.islower()):
        decrypt += chr((ord(char)-shift-97)% 26 + 97)
    elif(char.isupper()):
        decrypt += chr((ord(char)-shift-65)% 26 + 65)
    elif(char.isdigit()):
        decrypt += chr((ord(char)-shift-48)% 10 + 48)
    elif(char.isspace()):
        decrypt += ' '

print("Recieved data : ",decrypt)

# disconnect the client
s.close()
