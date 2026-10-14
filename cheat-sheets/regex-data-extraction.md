# Regular Expressions (Regex) Data Extraction Cheatsheet

> **Author**: Mohammad Bagus Satrio ([@bagusa13](https://github.com/bagusa13))  
> **Repository**: [developer-journal](https://github.com/bagusa13/developer-journal)

Pola Regular Expressions esensial untuk memparsing log, forensik data, dan otomasi ekstraksi teks.

---

## 1. Jaringan & Identitas (Network & Host)

| Target Data | Pola Regex | Deskripsi |
| :--- | :--- | :--- |
| **IPv4 Address** | `\b(?:(?:25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\b` | Mencocokkan valid IP 0.0.0.0 – 255.255.255.255 |
| **MAC Address** | `\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b` | Format `00:1A:2B:3C:4D:5E` atau `00-1A-2B-3C-4D-5E` |
| **Domain Name** | `\b(?=.{1,253}\b)(?:(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}\b` | Mencocokkan FQDN (misal `api.sub.domain.com`) |
| **URL (HTTP/HTTPS)** | `https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)` | Mencocokkan link URL lengkap |

---

## 2. Kriptografi & Hash Bukti Digital

| Format Hash | Panjang | Pola Regex |
| :--- | :--- | :--- |
| **MD5** | 32 Hex | `\b[a-fA-F0-9]{32}\b` |
| **SHA-1** | 40 Hex | `\b[a-fA-F0-9]{40}\b` |
| **SHA-256** | 64 Hex | `\b[a-fA-F0-9]{64}\b` |
| **JWT Token** | 3 Bagian Base64 | `\beyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\b` |

---

## 3. Format Tanggal & Timestamp Log

| Tipe Log | Contoh | Pola Regex |
| :--- | :--- | :--- |
| **ISO 8601 / UTC** | `2026-10-15T04:20:00Z` | `\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z\|[+-]\d{2}:\d{2})` |
| **Common Apache Log** | `[15/Oct/2026:04:20:00 +0000]` | `\[\d{2}\/[A-Za-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2}\s+[+-]\d{4}\]` |

---

## 4. Contoh Pemakaian Python (`re`)

```python
import re

log_line = '192.168.1.105 - - [15/Oct/2026:04:20:11 +0700] "GET /admin HTTP/1.1" 403 512'

ipv4_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
status_pattern = re.compile(r'"\s+(\d{3})\s+')

ip_match = ipv4_pattern.search(log_line)
status_match = status_pattern.search(log_line)

if ip_match and status_match:
    print(f"Detected IP: {ip_match.group()} | HTTP Status: {status_match.group(1)}")
```
