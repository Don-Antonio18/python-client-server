import socket
import threading
# server_hostname = socket.gethostbyname_ex(socket.gethostname())[0]  # local hostname
# server_ip = socket.gethostbyname_ex(socket.gethostname())[2][1]

def get_addr():
    i = str(input("What address should the message be sent to?: "))
    return i

def get_port():
    i = int(input("What port should the message be sent to?: "))
    return i

def encode_msg(msg):
    return msg.encode()

def decode_response(msg):
    return msg.decode()

def process_response():
    response, address = client_socket.recvfrom(2048)
    return response, address

def display_response(response, address):
    print(f"Server Response: '{response}'")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVER = get_addr()
PORT = get_port()
ADDR = (SERVER, PORT)
CONNECTED = True


while CONNECTED:

    msg = input("Write a message (exit to quit): ")
    encoded_msg = encode_msg(msg)
    client_socket.sendto(encoded_msg, (ADDR))

    if msg.lower() == "exit":
        CONNECTED = False

    response, address = process_response()
    response = decode_response(response)
    display_response(response, address)


client_socket.close()
