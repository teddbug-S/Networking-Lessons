
IP = ""  # your public ip


def server(ip):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((ip, 8080))
        print(f'[+] Server started with {ip} on 8080.')
        sock.listen(2)
        conn, (ip, port) = sock.accept()
        with conn:
            print(f"[+] Connection received from {ip} on port {port}.")
            while True:
                msg = conn.recv(1024)
                print(msg)
                response = bytes(input("Message: "), 'utf-8')
                if response == b'exit':
                    break
                conn.send(response)


if __name__ == '__main__':
    server(IP)
