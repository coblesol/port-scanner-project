🔍 Port Scanner Project
This is a multithreaded TCP port scanner written in Python 3. It allows users to scan a range of ports on a target IP address and optionally save the results to a text file.

The scanner uses threads to quickly check whether each port is open or closed, and can be used on Linux, macOS, or Windows (via PowerShell or terminal).

🚀 How to Run
bash
Copy code
python3 port_scanner.py --ip 127.0.0.1 --start-port 1 --end-port 1024 --threads 100 --output results.txt
Arguments:

--ip: Target IP address (required)

--start-port: Starting port (default is 1)

--end-port: Ending port (default is 1024)

--threads: Number of threads to use (default is 100)

--output: (Optional) Output file to log results

🛠 Branch Breakdown
main (⚙️ Full Scanner)
Most detailed version

Prints every port in range and shows whether it is OPEN or CLOSED

Logs results to a file if --output is passed

Best for learning and debugging, but slower than the others

advanced (⚡ Performance Focused)
Similar functionality to main but optimized for slightly faster execution

Intended to reduce output noise or integrate into automated tooling later

Still supports logging and threading

basic (🔹 Lightweight Version)
Minimalist version of the scanner

Still uses multithreading, but may only print open ports (depending on how you tweak it)

Great for quick scans or small scripts

✅ Example Output
bash
Copy code
Scanning 192.168.1.1 from port 1 to 1024 using 100 threads...
Port 22 is CLOSED
Port 80 is OPEN
Port 443 is OPEN
...
[+] Full results saved to results.txt
📌 Notes
Must be run with Python 3

Be sure to use responsibly — scanning unauthorized networks may be illegal

Let me know if you want the README in Markdown file format or if you want a version that only prints open ports for a quieter output.
