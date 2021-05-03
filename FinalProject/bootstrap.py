import json

config_dir = "configs\\"
topology_path = config_dir + "topology.json"
ports_path = config_dir + "ports.json"

# Build topology from JSON config files
topology = {}
for node in range(1,8):
    with open(config_dir + f"N{node}.json", "r") as f:
        data = json.load(f)
        for key, value in data.items():
            topology[key] = value

# Write topology to topology config file
with open(topology_path, "w") as f:
    json.dump(topology, f)

# Write unique ports of each node to config file
ports = {
    'N1': 65001,
    'N2': 65002,
    'N3': 65003,
    'N4': 65004,
    'N5': 65005,
    'N6': 65006,
    'N7': 65007
}
with open(ports_path, "w") as f:
    json.dump(ports, f)