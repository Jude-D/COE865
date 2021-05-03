import socket
import struct
import json

def get_send_socket(TTL=2):
    # Create UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set timeout
    sock.settimeout(1)

    # Set TTL
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, TTL)

    return sock

def get_receive_socket(MCAST_GROUP, PORT):
    # Create UDP Receiving socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to server address
    sock.bind(('', PORT))

    # Add socket to multicast group
    group = socket.inet_aton(MCAST_GROUP)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    return sock

def get_ports():
    ports = {}
    with open("configs\\ports.json", "r") as f:
        ports = json.load(f)

    return ports

def get_receiving_port(NODE, ports, tree):
    path_pair = tree[NODE]
    next_hop = path_pair[1]
    
    return ports[next_hop]