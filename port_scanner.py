#!/usr/bin/env python3
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                return port
    except Exception:
        return None

def main():
    parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
    parser.add_argument('--ip', required=True, help='Target IP address')
    parser.add_argument('--start-port', type=int, default=1, help='Start of port range (default: 1)')
    parser.add_argument('--end-port', type=int, default=1024, help='End of port range (default: 1024)')
    parser.add_argument('--threads', type=int, default=100, help='Number of threads (default: 100)')
    parser.add_argument('--output', help='Output file to save open ports')
    
    args = parser.parse_args()
    ip = args.ip
    start_port = args.start_port
    end_port = args.end_port
    threads = args.threads
    output_file = args.output

    print(f"Scanning {ip} from port {start_port} to {end_port} using {threads} threads...")

    open_ports = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda p: scan_port(ip, p), range(start_port, end_port + 1))

    for port, result in zip(range(start_port, end_port + 1), results):
        if result:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

    if output_file:
        with open(output_file, 'w') as f:
            for port in open_ports:
                f.write(f"Port {port} is OPEN\n")
        print(f"[+] Results saved to {output_file}")

if __name__ == '__main__':
    main()
