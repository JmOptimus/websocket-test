import socket
import json

UDP_PORT = 5005
UDP_IP = "https://data-consumer.onrender.com/"

data = {
    "stop": 1,
    "name": "55",
    "elevation": 0,
    "azimuth": 0,
}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(json.dumps(data).encode('utf-8'), (UDP_IP, UDP_PORT))
print("Data sent!")
