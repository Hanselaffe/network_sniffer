# Network Sniffer

A basic network sniffer that captures and analyzes network packets.

## Features

- Capture network packets on a specified interface.
- Analyze packets and display protocol, source IP, and destination IP.
- Web interface to start packet capture and view results.

## Prerequisites

- Python 3
- Pip
- Virtual Environment (optional but recommended)
- tshark 

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd network_sniffer

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    virtualenv venv
    source venv/bin/activate

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt


## Usage

1. Start the Flask app:
    ```sh
    python run.py

2. Open your web browser and navigate to http://127.0.0.1:5000/.

3. Enter the network interface and number of packets to capture, then start sniffing.

## Contributing
Contributions are welcome! Please create an issue before making changes and open a pull request for your changes.




