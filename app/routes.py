from flask import Blueprint, render_template, request
from sniffer.packet_sniffer import capture_packets
from sniffer.paket_analyzer import analyze_packet

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/sniff', methods=['POST'])
def sniff():
    interface = request.form['interface']
    packet_count = int(request.form['packet_count'])
    packets = capture_packets(interface, packet_count)
    results = [analyze_packet(packet) for packet in packets]
    return render_template('results.html', results=results)
