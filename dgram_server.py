import socket


DATA_SIZE = 1000

# creating a Datagram socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as dgram:
    # binding the socket to an ip and a port but in this case
    # I'll use the INADDR_ANY constant to allow any ip to connect
    dgram.bind((socket.INADDR_ANY, 2525))
    # receiving data from any client who tries to connect
    msg, (address, port) = dgram.recvfrom(DATA_SIZE)
    print(f"Connection started from {address} on port {port}.")
    # sending a response back to the client
    dgram.sendto(b"We have received your data.", (address, port))
