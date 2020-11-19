import socket

DATA_SIZE = 1000

# creating  a datagram client
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as dgram:
    # constructing a message
    msg = b"Hello server, please respond."
    # sending the message to the server
    print(f"[+]: Sending {msg} to the server.")
    dgram.sendto(msg, (socket.gethostname(), 2525))
    print("[SERVER]", dgram.recv(DATA_SIZE).decode('utf-8'))
