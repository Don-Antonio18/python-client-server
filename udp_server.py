import socket
import threading
import os

PORT = 5050
SERVER_HOSTNAME = socket.gethostname()
SERVER_IP = socket.gethostbyname_ex(socket.gethostname())[2][1]
SERVER = '0.0.0.0' # Covers all available interfaces
ADDR = (SERVER, PORT)
CONNECTED = True


def read_msg(server_socket):
    msg, client_addr = server_socket.recvfrom(2048)
    return msg, client_addr

def decode_msg(msg):
    return msg.decode('utf-8')

def display_msg(msg, client_addr):
    print(f"Received: '{msg}' from {client_addr}.")

def encode_response(msg):
    # add special msg processing  here + .encode()
    return msg.upper().encode()

def send_response(msg, client_addr, server_socket):
    server_socket.sendto(msg, client_addr)
    print(f"Response sent to {client_addr}..")

def exit_msg():
    return f"Closing connection"

def disconnect_msg(client_addr):
    return f"{client_addr} has disconnected."


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER, PORT))

    print(f"Server Name:{SERVER_HOSTNAME}/{SERVER_IP} Port:{PORT}")
    try:
        while True:
            msg, client_addr = read_msg(server_socket)
            thread = threading.Thread(target=handle_request, args=(msg, client_addr, server_socket))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("Shutting down server...\n Server offline.")
    finally:
        server_socket.close()
        print("Shutting down server...\n Server offline.")


def handle_request(msg, client_addr, server_socket):
    if not msg: return # empty message fallback
    msg = decode_msg(msg)
    
    if msg.lower() == "exit":
        server_socket.sendto(exit_msg().encode(), client_addr)
        print(disconnect_msg(client_addr))
        return # Ends thread session

    # rickroll
    elif msg == "never gonna give you up":
        print("never gonna let you down!")
        print("(remote shutdown activated)")
        os._exit(0)

    else:
        display_msg(msg, client_addr)
        encoded_msg = encode_response(msg)
        send_response(encoded_msg, client_addr, server_socket)


if __name__ == "__main__":
        start_server()
