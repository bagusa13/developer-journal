# 🐧 Linux Privilege Escalation & Audit Cheatsheet

Referensi audit keamanan sistem operasi Linux dan identifikasi vektor eskalasi hak akses (*Privilege Escalation*).

---

## 1. Audit SUID / SGID Binaries
Binari dengan bit SUID berjalan dengan hak akses root:
```bash
find / -perm -u=s -type f 2>/dev/null
```
*Cek apakah binari yang ditemukan terdaftar di [GTFOBins](https://gtfobins.github.io/) untuk bypass shell.*

---

## 2. Pemeriksaan Hak Akses Sudo
```bash
# Periksa perintah apa saja yang diizinkan dijalankan sebagai root tanpa password
sudo -l
```

---

## 3. Pemeriksaan Scheduled Tasks (Cron Jobs)
```bash
# Periksa file cron sistem
cat /etc/crontab
ls -la /etc/cron.*

# Cari script cron yang memiliki izin tulis publik (writable by all)
find /etc/cron* -type f -writable 2>/dev/null
```
