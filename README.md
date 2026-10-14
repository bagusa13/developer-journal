# Developer Guidebook & Scripting Playbook

[![Author](https://img.shields.io/badge/Author-Mohammad%20Bagus%20Satrio-blue?style=for-the-badge&logo=github)](https://github.com/bagusa13)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Focus](https://img.shields.io/badge/Stack-Python%20%7C%20Bash%20%7C%20PowerShell-orange?style=for-the-badge)](https://github.com/bagusa13)
[![Domain](https://img.shields.io/badge/Domain-Automation%20%7C%20Sysadmin%20%7C%20DFIR-red?style=for-the-badge)](https://github.com/bagusa13)

Selamat datang di repositori **buku pedoman developer (*developer guidebook*)** dan resep otomasi yang dikurasi oleh **Mohammad Bagus Satrio**. 

Repositori ini berfungsi sebagai referensi standar, template rancang bangun script (*Python, Bash, PowerShell*), resep otomasi produksi, dan kumpulan *cheat sheets* teknis harian untuk memastikan setiap script dan perkakas yang dibangun memiliki arsitektur yang rapi, modular, *fault-tolerant*, dan berstandar industri.

---

## 📂 Struktur Repositori

```text
developer-journal/
|-- scripting-templates/               # Starter Boilerplates Berstandar Produksi
|   |-- python_script_template.py      # Standard CLI dengan argparse, logging, & exit codes
|   |-- bash_script_template.sh        # Bash strict mode (set -euo pipefail) & signal traps
|   `-- powershell_template.ps1        # PowerShell CmdletBinding, validation, & error handling
|-- automation-and-tools/              # Utilitas & Resep Otomasi Siap Pakai
|   |-- api_client_resilient.py        # HTTP client dengan exponential backoff retry
|   |-- evidence_hasher.py             # Multi-hash integrity verifier (MD5, SHA-1, SHA-256)
|   |-- network_triage.py              # Rapid socket listener & port inspector
|   `-- requirements.txt               # Daftar dependensi Python
|-- cheat-sheets/                      # Pedoman Sintaks Cepat & Best Practices
|   |-- python-best-practices.md       # Clean code, type hints, pathlib, & context managers
|   |-- bash-automation-guide.md       # Linux stream processing (awk, sed, xargs, grep)
|   |-- powershell-cheatsheet.md       # Pipeline objek Windows & administrasi sistem
|   |-- regex-data-extraction.md       # Pola regex esensial (IP, hash, email, timestamp)
|   `-- git-workflow-guide.md          # Conventional commits & git hygiene
`-- security-and-dfir/                 # Modul Keamanan Siber & Digital Forensik
    |-- memory-forensics-volatility.md # Volatility 3 RAM analysis cheat sheet
    |-- usb-artifact-carving-guide.md  # File carving & USB partition anatomy
    |-- wireshark-filters-guide.md     # Filter inspeksi traffic Wireshark
    `-- linux-security-cheatsheet.md   # Linux audit & privilege escalation checklist
```

---

## 🛠️ Prinsip Desain Script (Engineering Standards)

Setiap script dan modul dalam repositori ini dibangun mengikuti empat pilar:

1. **Input Parsing yang Ketat (*Strict Input Handling*)**:
   Menggunakan parser bawaan bahasa (`argparse` di Python, `getopts` di Bash, `param()` di PowerShell) lengkap dengan bantuan (`--help`), tipe data jelas, dan pesan error jika argumen kurang.
2. **Logging Terstruktur (*Structured Logging*)**:
   Tidak menggunakan perintah cetak mentah (`print`). Menggunakan level log terstandar (`INFO`, `WARNING`, `ERROR`, `DEBUG`) dengan format timestamp ISO yang konsisten.
3. **Exit Codes Deterministik**:
   Mengembalikan kode status Unix yang tepat (`0` untuk sukses, `1` untuk galat runtime, `2` untuk kesalahan argumen, `130` untuk interupsi pengguna).
4. **Pembersihan Resource Otomatis (*Graceful Teardown*)**:
   Menjamin file descriptor, koneksi soket, dan file sementara selalu ditutup/dibersihkan melalui `with` context manager atau signal `trap`.

---

## 🚀 Panduan Cepat Menjalankan Perkakas

### 1. Forensic Evidence Hasher
Menghitung hash kriptografis (*MD5, SHA-1, SHA-256*) bukti file atau direktori secara massal:
```bash
python automation-and-tools/evidence_hasher.py /path/to/target -o hash_report.json
```

### 2. Network Socket Triage
Audit port aktif dan listening service pada host target:
```bash
python automation-and-tools/network_triage.py 127.0.0.1
```

### 3. Resilient API Client
Mengirim request HTTP dengan automatic retry dan exponential backoff:
```bash
python automation-and-tools/api_client_resilient.py https://api.github.com/zen --retries 3
```

---

## 🔗 Proyek Terkait

- **[dfir-usb-investigation](https://github.com/bagusa13/dfir-usb-investigation)**: Analisis forensik fisik USB drive, MBR/exFAT parsing, file carving, dan anti-forensics.

---

## 👤 Author & Kontak

- **Nama**: Mohammad Bagus Satrio
- **Email**: [bagusa1313@gmail.com](mailto:bagusa1313@gmail.com)
- **GitHub**: [@bagusa13](https://github.com/bagusa13)
- **LinkedIn**: [linkedin.com/in/bagusa](https://www.linkedin.com/in/bagusa)
