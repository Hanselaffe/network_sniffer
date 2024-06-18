import pyshark

def capture_packets(interface, packet_count):
    capture = pyshark.LiveCapture(interface=interface, tshark_path='/usr/bin/tshark')
    capture.sniff(packet_count=packet_count)
    packets = [packet for packet in capture]
    return packets

def start_sniffing(interface, packet_count, callback):
    capture = pyshark.LiveCapture(interface=interface, tshark_path='/usr/bin/tshark')
    capture.sniff(packet_count=packet_count)
    for packet in capture:
        callback(packet)
