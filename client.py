import socket
from tkinter import *
from threading import Thread

class GUI:
    def __init__(self):
        self.Window = TK()
        self.Window.withdraw()
        
        self.login = Toplevel()
        self.login.title("login")
        
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        
        self.pls = Label(self.login,
                    text = "pls login to continue",
                    justify=CENTER,
                    font="helvetica 14 bold"

        )
        




#nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

#def receive():
    #while True:
        #try:
            #message = client.recv(2048).decode('utf-8')
           # if message == 'NICKNAME':
              #  client.send(nickname.encode('utf-8'))
            #else:
              #  print(message)
        #except:
          #  print("An error occured!")
            #client.close()
           # break

#def write():
    #while True:
        #message = '{}: {}'.format(nickname, input(''))
        #client.send(message.encode('utf-8'))

#receive_thread = Thread(target=receive)
#receive_thread.start()
#write_thread = Thread(target=write)
#write_thread.start()
