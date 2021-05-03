import sys
from multicast import get_send_socket, get_receive_socket, get_ports, get_receiving_port
from path import get_minimum_cost_tree, get_next_nodes

if len(sys.argv) != 2:
    print("Invalid arguments")
    sys.exit()

# Get shortest path tree
tree = get_minimum_cost_tree()

# Get ports
ports = get_ports()

# Initialize node, multicast group
NODE = f'N{sys.argv[1]}'
MCAST_GROUP = '224.86.5.5'

# Get receiving and sending ports
PORT_R = get_receiving_port(NODE, ports, tree)
PORT_S = ports[NODE]

# Create UDP Receiving/Sending Sockets
sock_R = get_receive_socket(MCAST_GROUP, PORT_R)
sock_S = get_send_socket()

# Receive message and send to receiver(s)
try:
    print(f'FORWARDER {NODE}')
    while True:
        # Receive message
        data, address = sock_R.recvfrom(1024)
        print(f'"{data.decode()}" from {address}')

        # Send data to receiver
        next_nodes = get_next_nodes(tree, NODE)
        receiving_nodes = " and ".join(next_nodes)
        print('Sending Data To RECEIVER ' + receiving_nodes + '\n')
        sent = sock_S.sendto(data, (MCAST_GROUP, PORT_S))
finally:
    print('Closing Sending/Receiving Socket')
    sock_S.close()
    sock_R.close()