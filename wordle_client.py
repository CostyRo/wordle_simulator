import socket

SERVER=socket.gethostbyname(socket.gethostname())
PORT=8555

if __name__=="__main__":
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as connection:
        connection.connect((SERVER,PORT))

        connection.send(input().upper().encode())
        print(connection.recv(5).decode("utf-8"))
