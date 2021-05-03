import sys
from multicast import get_receive_socket, get_ports, get_receiving_port
from path import get_minimum_cost_tree

if len(sys.argv) != 2:
    print("Invalid arguments")
    sys.exit()

# Get shortest path tree
tree = get_minimum_cost_tree()

# Get ports
ports = get_ports()

# Initialize node, multicast group, port
NODE = f'N{sys.argv[1]}'
MCAST_GROUP = '224.86.5.5'
PORT = get_receiving_port(NODE, ports, tree)

# Create UDP Receiving Socket
sock = get_receive_socket(MCAST_GROUP, PORT)

# Receive message
try:
    print(f'RECEIVER {NODE}')
    while True:
        data, address = sock.recvfrom(1024)
        print(f'Address/Port: {address}')
        print(f'Message: {data.decode()}\n')
finally:
    print('Closing Socket\n')
    sock.close()