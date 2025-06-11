# 🔍 Port Scanner Project

A fast, multithreaded TCP port scanner written in Python 3. It scans a range of ports on a given IP address and optionally saves the results to a text file.

This scanner works on **Linux**, **macOS**, and **Windows** (via PowerShell or terminal), using Python's `socket` and `concurrent.futures` modules for performance.

---

## 🚀 How to Run

```bash
python3 port_scanner.py --ip 127.0.0.1 --start-port 1 --end-port 1024 --threads 100 --output results.txt
Arguments
--ip: Target IP address (required)

--start-port: Starting port (default: 1)

--end-port: Ending port (default: 1024)

--threads: Number of threads (default: 100)

--output: (Optional) File path to save results

🛠 Branch Breakdown
main (⚙️ Full Scanner)
Scans all ports in range and prints both OPEN and CLOSED ports

Supports saving full results to file

Best for full visibility and logging

advanced (⚡ Performance Optimized)
Similar to main, but optimized for speed

Quieter output; easier to integrate into scripts or automation

Still uses threading and logging

basic (🔹 Lightweight Version)
Stripped-down version

May only display open ports

Ideal for fast scans and simpler use cases

✅ Example Output
bash
Scanning 192.168.1.1 from port 1 to 1024 using 100 threads...
Port 22 is CLOSED
Port 80 is OPEN
Port 443 is OPEN
...
[+] Full results saved to results.txt
📌 Notes
Requires Python 3
