#!/usr/bin/env python3
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            return (port, result == 0)  # (port, is_open)
    except Exception:
        return (port, False)

def main():
    parser = argparse.ArgumentParser(description="Full TCP Port Scanner with Logging")
    parser.add_argument('--ip', required=True, help='Target IP address')
    parser.add_argument('--start-port', type=int, default=1, help='Start of port range (default: 1)')
    parser.add_argument('--end-port', type=int, default=1024, help='End of port range (default: 1024)')
    parser.add_argument('--threads', type=int, default=100, help='Number of threads (default: 100)')
    parser.add_argument('--output', help='Output file to save results')
    
    args = parser.parse_args()
    ip = args.ip
    start_port = args.start_port
    end_port = args.end_port
    threads = args.threads
    output_file = args.output

    print(f"Scanning {ip} from port {start_port} to {end_port} using {threads} threads...")

    results = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = list(executor.map(lambda p: scan_port(ip, p), range(start_port, end_port + 1)))

    for port, is_open in results:
        status = "OPEN" if is_open else "CLOSED"
        print(f"Port {port} is {status}")

    if output_file:
        with open(output_file, 'w') as f:
            for port, is_open in results:
                status = "OPEN" if is_open else "CLOSED"
                f.write(f"Port {port} is {status}\n")
        print(f"[+] Full results saved to {output_file}")

if __name__ == '__main__':
    main()
