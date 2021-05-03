from multicast import get_send_socket, get_ports
from path import get_minimum_cost_tree

# Get shortest path tree
tree = get_minimum_cost_tree()

# Get ports
ports = get_ports()

# Initialize node, multicast group, port
NODE = 'N1'
MCAST_GROUP = '224.86.5.5'
PORT = ports[NODE]

# Create UDP Sending Socket
sock = get_send_socket()

try:
    print(f'SOURCE {NODE}')

    while True:
        # Collect Message
        message = input('Enter message: ')
        if not message:
            print('Terminating')
            break

        # Send data
        sent = sock.sendto(message.encode(), (MCAST_GROUP, PORT))
finally:
    print('Closing Socket')
    sock.close()