#!/usr/bin/python3
import socket

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 7877


srv_sock.bind((host,port))

srv_sock.listen(10)

conn,addr = srv_sock.accept()

print(conn)
print('accept client addr :',addr)
conn.send('Your connection is admited.'.encode('utf-8'))


while True :
        msg_get = conn.recv(1024).decode('utf-8')
        if len(msg_get) <= 0 :
            continue
        elif msg_get == 'quit' :
            print('client %s quit.', addr )
            break
        else :
            print('Get msg from client: ', msg_get)
conn.close()
srv_sock.close()




