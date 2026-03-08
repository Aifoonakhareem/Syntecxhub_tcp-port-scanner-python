import socket

host = "127.0.0.1"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Server listening on port 9999...")

while True:
    conn, addr = server.accept()
    print("Connection from", addr)
    conn.send(b"Test server running\n")
    conn.close()