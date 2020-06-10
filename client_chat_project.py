import socket
import threading
import os
client=socket.socket()
client.connect(("192.168.43.77",1234))
print("Connected to server\n\n")
os.system("cls")
print("-"*60)
print("Welcome to InstaChat".center(60))
print("This is Chirag's Screen".center(60))
print("-"*60)
def send(client):
    while True:
        msg=input('Chirag--->'.rjust(55,' '))
        client.send(msg.encode())
        if msg.lower()=='bye':
            break
            
def recv(client):
    while True:
        msg=client.recv(1024).decode()
        print(f'Karan---->{msg}')
        if msg=='bye':
            break

t1=threading.Thread(target=send,args=(client,))
t2=threading.Thread(target=recv,args=(client,))

t1.start()
t2.start()

t1.join()
t2.join()

client.close()
