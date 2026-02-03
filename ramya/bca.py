import socket
import threading

HOST = "127.0.0.1"
PORT = 5555


def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                print("\nFriend:", message)
        except:
            print("\nConnection closed.")
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print("Server started... Waiting for connection")

    conn, addr = server.accept()
    print("Connected with", addr)

    threading.Thread(target=receive_messages, args=(conn,)).start()

    while True:
        msg = input("You: ")
        conn.send(msg.encode())


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        msg = input("You: ")
        client.send(msg.encode())


choice = input("Type 'server' to start server or 'client' to connect: ")

if choice.lower() == "server":
    start_server()
else:
    start_client()
