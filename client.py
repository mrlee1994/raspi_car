#!/usr/bin/python3
import socket
import time

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 7877
host = socket.gethostname()
cli_sock.connect((host , port))

cli_sock.send('hello, server'.encode('utf-8'))
while True :
    str = input(">> ")
    cli_sock.send(str.encode('utf-8'))
    if str.lower() == 'quit' :
        break
time.sleep(5)
cli_sock.close()
