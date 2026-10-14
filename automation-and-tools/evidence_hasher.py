#!/usr/bin/env python3
"""
Evidence Hasher & Integrity Verifier
Author: Mohammad Bagus Satrio (https://github.com/bagusa13)
Repository: developer-journal
Purpose: Forensic-grade multi-hash generation (MD5, SHA-1, SHA-256) with chain-of-custody logging.
"""

import os
import sys
import hashlib
import json
import argparse
from datetime import datetime

CHUNK_SIZE = 65536  # 64 KB reading buffer

def calculate_hashes(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    file_size = os.path.getsize(file_path)

    with open(file_path, 'rb') as f:
        while chunk := f.read(CHUNK_SIZE):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    return {
        "file_name": os.path.basename(file_path),
        "absolute_path": os.path.abspath(file_path),
        "file_size_bytes": file_size,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "hashes": {
            "md5": md5.hexdigest(),
            "sha1": sha1.hexdigest(),
            "sha256": sha256.hexdigest()
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Forensic-grade Evidence Hasher")
    parser.add_argument("target", help="Path to evidence file or directory to hash")
    parser.add_argument("-o", "--output", help="Export results to JSON report file", default=None)
    args = parser.parse_args()

    results = []
    if os.path.isfile(args.target):
        results.append(calculate_hashes(args.target))
    elif os.path.isdir(args.target):
        for root, _, files in os.walk(args.target):
            for file in files:
                p = os.path.join(root, file)
                try:
                    results.append(calculate_hashes(p))
                except Exception as e:
                    print(f"[!] Error hashing {p}: {e}", file=sys.stderr)
    else:
        print(f"[!] Invalid path: {args.target}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(results, indent=2))

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as out:
            json.dump(results, out, indent=2)
        print(f"\n[+] Forensic hash report saved to: {args.output}")

if __name__ == "__main__":
    main()
