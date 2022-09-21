import socket

port = 1024
ip = ''
s=socket.socket()
print("Socket successfully created")
s.bind((ip,port))
print("Scoket binded to %s" %(port))
s.listen(5)
print("Socket is listening")
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode())
    c.close()
    break