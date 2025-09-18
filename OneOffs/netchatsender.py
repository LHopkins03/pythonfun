import socket

host = "127.0.0.1"
port = 8080
userID = input("Enter your username:\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Enter q alone to quit at anytime")

chatInput = input()
while chatInput != "q":
    chatInput = userID + ': ' + chatInput
    s.send(chatInput.encode('utf-8'))
    chatInput = input()
