import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("", 8080))
    print('[+] Connected to server successfully.')
    while True:
        msg = bytes(input("Message: "), 'utf-8')
        sock.send(msg)
        response = str(sock.recv(1024))
        print(response)
