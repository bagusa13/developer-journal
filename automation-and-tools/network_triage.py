#!/usr/bin/env python3
"""
Lightweight Network Triage & Port Inspector
Author: Mohammad Bagus Satrio (https://github.com/bagusa13)
Repository: developer-journal
Purpose: Fast local socket and listening services identification for incident response and sysadmin triage.
"""

import socket
import argparse
from datetime import datetime

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"
}

def scan_port(host, port, timeout=0.8):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                service = COMMON_PORTS.get(port, "Unknown Service")
                return port, True, service
    except Exception:
        pass
    return port, False, None

def main():
    parser = argparse.ArgumentParser(description="Network Socket Triage Checker")
    parser.add_argument("host", help="Target IP or hostname to audit (e.g. 127.0.0.1)")
    args = parser.parse_args()

    print(f"[*] Starting network triage on: {args.host}")
    print(f"[*] Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"{'PORT':<8} {'STATUS':<10} {'SERVICE'}")
    print("-" * 32)

    open_ports = 0
    for port in sorted(COMMON_PORTS.keys()):
        p, is_open, service = scan_port(args.host, port)
        if is_open:
            print(f"{p:<8} {'OPEN':<10} {service}")
            open_ports += 1

    print("-" * 32)
    print(f"[+] Scan complete. Total active listeners: {open_ports}")

if __name__ == "__main__":
    main()
