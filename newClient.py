import socket
import sys

HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])
data = input("Enter the string to be sent: ")

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    print("Sent:\"{}\"".format(data))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

if(data.startswith('W')):
    print("The number of words is: {}".format(received))
elif(data.startswith('L')):
    print("The number of lowercase letters is: {}".format(received))
elif(data.startswith('U')):
    print("The number of uppercase letters is: {}".format(received))
elif(data.startswith('R')):
    print("The number of numeric characters is: {}".format(received))
elif(data.startswith('T')):
    print("The number of characters is: {}".format(received))
else:
    print(f"Received: {received}")