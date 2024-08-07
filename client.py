import socket

# take the server name and port name
host = 'local host'
port = 5000

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

# wait till a client accept
# connection
c, addr = s.accept()

# display client address
print("CONNECTION FROM:", str(addr))

letter = input("Enter the data : ")
shift = 3
encrypt = ''

for char in letter:
    if(char.islower()):
        encrypt += chr((ord(char)+shift-97)% 26 + 97)
    elif(char.isupper()):
        encrypt += chr((ord(char)+shift-65)% 26 + 65)
    elif(char.isdigit()):
        encrypt += chr((ord(char)+shift-48)% 10 + 48)
    elif(char.isspace()):
        encrypt += ' '


# send message to the client after 
# encoding into binary string
c.send(encrypt.encode())


# disconnect the server
c.close()
