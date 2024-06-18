def analyze_packet(packet):
    try:
        protocol = packet.highest_layer
        src_ip = packet.ip.src
        dst_ip = packet.ip.dst
        info = f"Protocol: {protocol}, Source IP: {src_ip}, Destination IP: {dst_ip}"
        return info
    except AttributeError as e:
        return "Packet does not have IP layer information."
