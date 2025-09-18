import socket

host = "127.0.0.1"
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received:", data.decode('utf-8'))