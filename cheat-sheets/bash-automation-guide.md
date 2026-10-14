# Linux & Bash Automation Playbook

> **Author**: Mohammad Bagus Satrio ([@bagusa13](https://github.com/bagusa13))  
> **Repository**: [developer-journal](https://github.com/bagusa13/developer-journal)

Koleksi teknik, perintah satu baris (*one-liners*), dan pemrosesan stream data teks untuk otomasi shell Linux.

---

## 1. Golden Rule: Unofficial Strict Mode

Selalu tempatkan deklarasi ini di baris teratas script bash setelah shebang:

```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
```
- `-e`: Keluar seketika jika ada perintah yang menghasilkan exit code bukan 0.
- `-u`: Lempar error jika mengakses variabel yang belum dideklarasikan (*unbound variable*).
- `-o pipefail`: Gagalkan pipeline jika salah satu perintah di rantai `|` gagal.
- `IFS`: Mencegah pemisahan string berbasis spasi yang merusak looping nama file.

---

## 2. Text Stream Processing (`awk`, `sed`, `cut`, `grep`)

### Mengambil Kolom Tertentu dengan `awk`
```bash
# Menampilkan IP address dan status dari output netstat/ss
ss -tuln | awk '{print $1, $5}'

# Menghitung total ukuran file (kolom 5) dari ls -l
ls -l | awk '{sum += $5} END {print "Total bytes: " sum}'
```

### Manipulasi Teks dengan `sed`
```bash
# Mengganti kata kunci di seluruh file tanpa membuka editor
sed -i 's/PORT=3000/PORT=8080/g' .env

# Menghapus baris kosong atau baris komentar (#)
sed -e '/^#/d' -e '/^$/d' config.conf
```

### Pemfilteran Tingkat Lanjut dengan `grep`
```bash
# Ekstrak seluruh IP address (IPv4) dari file log
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' access.log | sort | uniq -c | sort -nr
```

---

## 3. Eksekusi Paralel & Batch (`xargs` & `parallel`)

```bash
# Menghitung hash SHA-256 untuk semua file .log secara paralel (4 thread)
find /var/log -type f -name "*.log" | xargs -P 4 -I {} sha256sum "{}"

# Menghapus file sementara yang berumur lebih dari 7 hari
find /tmp/uploads -type f -mtime +7 -delete
```

---

## 4. Signal Trapping & Graceful Cleanup

Gunakan `trap` untuk membersihkan direktori temporary saat script dihentikan:

```bash
TEMP_DIR=$(mktemp -d /tmp/audit.XXXXXX)

cleanup() {
    echo "[!] Cleaning up temporary assets: ${TEMP_DIR}"
    rm -rf "${TEMP_DIR}"
}
trap cleanup EXIT INT TERM
```
