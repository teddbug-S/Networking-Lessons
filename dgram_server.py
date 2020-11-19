import socket


DATA_SIZE = 1000
MSG = b"Hey client, we have received your data."

# creating a Datagram socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as dgram:
    # binding the socket to an ip and a port but in this case
    # I'll use empty quotes to allow any ip to connect
    dgram.bind((socket.gethostname(), 2525))
    # receiving data from any client who tries to connect
    msg, (address, port) = dgram.recvfrom(DATA_SIZE)
    print(f"[+]: Connection established from {address} on port {port}.")
    print(f"[+]: Sending {MSG} to client")
    # sending a response back to the client
    dgram.sendto(MSG, (address, port))
