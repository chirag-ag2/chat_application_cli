import socket
import threading
import os

server=socket.socket()

server.bind(('192.168.43.77',1234))

server.listen()
print("server: 192.168.43.77:1234")
client,addr=server.accept()
print(f"\nClient: {addr[0]}:{addr[1]}")
os.system("cls")
print("-"*60)
print("Welcome to InstaChat".center(60))
print("This is Karan's Screen".center(60))
print("-"*60)

def send(client):
    while True:
        msg=input('Karan--->'.rjust(55,' '))
        client.send(msg.encode())
        if msg.lower()=='bye':
            break
            
def recv(client):
    while True:
        msg=client.recv(1024).decode()
        print(f'Chirag--->{msg}')
        if msg=='bye':
            break

t1=threading.Thread(target=send,args=(client,))
t2=threading.Thread(target=recv,args=(client,))

t1.start()
t2.start()

t1.join()
t2.join()

client.close()
server.close()