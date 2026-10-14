# ðŸ§  Volatile Memory Forensics Cheatsheet (Volatility 3)

Panduan praktis investigasi dump RAM (*volatile memory forensics*) menggunakan framework Volatility 3 untuk mendeteksi proses mencurigakan, rootkit, dan injeksi kode (*code injection*).

---

## 1. Identifikasi Proses & Hirarki
`ash
# Daftar proses aktif
vol -f memory.dmp windows.pslist

# Pohon proses (melihat parent-child PID untuk mendeteksi impersonasi)
vol -f memory.dmp windows.pstree

# Menemukan proses siluman yang disembunyikan lewat unlinking DKOM
vol -f memory.dmp windows.psscan
`

---

## 2. Investigasi Koneksi Jaringan & Soket
`ash
# Menampilkan koneksi TCP/UDP aktif beserta PID pemiliknya
vol -f memory.dmp windows.netscan
`

---

## 3. Deteksi Injeksi Kode & Malware Memory
`ash
# Mendeteksi DLL injection / reflective injection (halaman memori PAGE_EXECUTE_READWRITE)
vol -f memory.dmp windows.malfind

# Dump memory proses tertentu berdasarkan PID
vol -f memory.dmp -o output_dir windows.dumpfiles --pid <PID>
`
"@ | Set-Content -Path "D:\02_File\developer-journal\forensics-dfir\memory-forensics-volatility.md" -Encoding UTF8

# 7. Dokumen Network Security: wireshark-filters-guide.md
@"
# ðŸŒ Network Traffic Analysis & Wireshark Filter Cheatsheet

Daftar filter penting (*display filters*) untuk analisis paket jaringan dalam skenario investigasi insiden (*Incident Response*).

---

## 1. Analisis DNS Anomali & Tunneling
`wireshark
# Tampilkan seluruh query DNS yang dikirim
dns.flags.response == 0

# Deteksi query TXT mencurigakan (sering digunakan DNS C2 tunneling)
dns.qry.type == 16

# Filter domain tertentu
dns.qry.name contains "malicious-domain.com"
`

---

## 2. Investigasi HTTP & Web Payload
`wireshark
# Mencari seluruh request HTTP method POST (biasanya upload payload atau submit kredensial)
http.request.method == "POST"

# Mencari file yang diunduh via HTTP
http.response.code == 200 and http.content_type contains "application"

# Cari kata sandi dalam lalu lintas HTTP plain-text
frame contains "password" or frame contains "passwd" or frame contains "login"
`

---

## 3. Deteksi Pemindaian Jaringan (Port Scanning)
`wireshark
# Deteksi paket TCP SYN tanpa ACK (indikasi SYN stealth scan)
tcp.flags.syn == 1 and tcp.flags.ack == 0

# Deteksi paket TCP RST (koneksi ditolak oleh host target)
tcp.flags.reset == 1
`
"@ | Set-Content -Path "D:\02_File\developer-journal\network-security\wireshark-filters-guide.md" -Encoding UTF8

# 8. Dokumen Linux Hardening: linux-security-cheatsheet.md
@"
# ðŸ§ Linux Privilege Escalation & Audit Cheatsheet

Referensi audit keamanan sistem operasi Linux dan identifikasi vektor eskalasi hak akses (*Privilege Escalation*).

---

## 1. Audit SUID / SGID Binaries
Binari dengan bit SUID berjalan dengan hak akses root:
`ash
find / -perm -u=s -type f 2>/dev/null
`
*Cek apakah binari yang ditemukan terdaftar di [GTFOBins](https://gtfobins.github.io/) untuk bypass shell.*

---

## 2. Pemeriksaan Hak Akses Sudo
`ash
# Periksa perintah apa saja yang diizinkan dijalankan sebagai root tanpa password
sudo -l
`

---

## 3. Pemeriksaan Scheduled Tasks (Cron Jobs)
`ash
# Periksa file cron sistem
cat /etc/crontab
ls -la /etc/cron.*

# Cari script cron yang memiliki izin tulis publik (writable by all)
find /etc/cron* -type f -writable 2>/dev/null
`
"@ | Set-Content -Path "D:\02_File\developer-journal\linux-administration\linux-security-cheatsheet.md" -Encoding UTF8

# 9. Dokumen Web Security: owasp-top10-guide.md
@"
# ðŸ›¡ï¸ OWASP Top 10 Web Application Security Summary

Ringkasan celah keamanan aplikasi web paling kritis dan mitigasi arsitekturnya.

---

## 1. Broken Access Control (A01:2021)
- **Celah**: Pengguna biasa dapat mengakses resource/data milik pengguna lain dengan memodifikasi ID pada URL/API (*IDOR - Insecure Direct Object References*).
- **Mitigasi**: Selalu verifikasi token sesi di sisi server (*server-side authorization*) sebelum mengembalikan data dari database.

---

## 2. Cryptographic Failures (A02:2021)
- **Celah**: Transmisi data sensitif via HTTP biasa atau hashing password menggunakan algoritma lemah (MD5/SHA1).
- **Mitigasi**: Gunakan TLS 1.3, hashing password dengan algoritma adaptif seperti **Argon2id** atau **Bcrypt** (work factor $\ge 12$).

---

## 3. Injection (SQLi, Command Injection, XSS) (A03:2021)
- **Celah**: Input pengguna langsung digabungkan ke query database atau perintah shell tanpa sanitasi.
- **Mitigasi**: Gunakan *Parameterized Queries* / ORM (seperti Prisma atau Sequelize), serta *Context-Aware Output Encoding*.
