# Cybersecurity, DFIR & Engineering Knowledge Base

[![Author](https://img.shields.io/badge/Author-Mohammad%20Bagus%20Satrio-blue?style=for-the-badge&logo=github)](https://github.com/bagusa13)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Focus](https://img.shields.io/badge/Domain-Cybersecurity%20%7C%20DFIR%20%7C%20Fullstack-red?style=for-the-badge)](https://github.com/bagusa13)

Selamat datang di repositori dokumentasi teknis, riset keamanan siber, catatan investigasi digital forensik (*DFIR*), dan perangkat utilitas kode terbuka yang dikurasi oleh **Mohammad Bagus Satrio**.

---

## Struktur Repositori

```text
developer-journal/
|-- forensics-dfir/                # Panduan Investigasi Forensik Digital
|   |-- usb-artifact-carving-guide.md
|   `-- memory-forensics-volatility.md
|-- network-security/              # Analisis Lalu Lintas Jaringan & Packet Inspection
|   `-- wireshark-filters-guide.md
|-- linux-administration/          # Hardening Sistem Operasi Linux & Privilege Escalation
|   `-- linux-security-cheatsheet.md
|-- web-security/                  # Praktik Keamanan Web & Arsitektur OWASP
|   `-- owasp-top10-guide.md
`-- scripts-and-tools/             # Perkakas Kode Otomasi Python (Standar DFIR)
    |-- evidence_hasher.py         # Multi-hash Integrity Verification Tool
    |-- network_triage.py          # Fast Socket & Port Listener Auditor
    `-- requirements.txt
```

---

## Perkakas Otomasi Bawaan (Scripts & Tools)

### 1. `evidence_hasher.py` (Forensic File Hasher)
Script Python untuk menghitung nilai hash kriptografis (*MD5, SHA-1, SHA-256*) bukti digital secara massal dengan output JSON berstandar forensik.

```bash
python scripts-and-tools/evidence_hasher.py /path/to/evidence -o report.json
```

### 2. `network_triage.py` (Socket Auditor)
Utilitas inspeksi port aktif untuk mengaudit socket lokal selama proses penanganan insiden (*Incident Response*).

```bash
python scripts-and-tools/network_triage.py 127.0.0.1
```

---

## Portofolio & Proyek Terkait

- **[dfir-usb-investigation](https://github.com/bagusa13/dfir-usb-investigation)**: Analisis forensik fisik USB drive, MBR/exFAT parsing, file carving, dan anti-forensics.
- **[kediengaja](https://github.com/bagusa13/kediengaja)**: Platform reservasi tur wisata berbasis Next.js 14, Firebase, dan WhatsApp engine.

---

## Author & Kontak

- **Nama**: Mohammad Bagus Satrio
- **Email**: [bagusa1313@gmail.com](mailto:bagusa1313@gmail.com)
- **LinkedIn**: [linkedin.com/in/bagusa](https://www.linkedin.com/in/bagusa)
- **GitHub**: [@bagusa13](https://github.com/bagusa13)
