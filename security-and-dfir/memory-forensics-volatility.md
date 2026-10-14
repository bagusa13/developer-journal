# Volatile Memory Forensics Cheatsheet (Volatility 3)

> **Author**: Mohammad Bagus Satrio ([@bagusa13](https://github.com/bagusa13))  
> **Repository**: [developer-journal](https://github.com/bagusa13/developer-journal)

Panduan praktis investigasi dump RAM (*volatile memory forensics*) menggunakan framework Volatility 3 untuk mendeteksi proses mencurigakan, rootkit, dan injeksi kode (*code injection*).

---

## 1. Identifikasi Proses & Hirarki

```bash
# Menampilkan daftar proses aktif saat dump diambil
vol -f memory.dmp windows.pslist

# Menampilkan pohon proses (melihat relasi parent-child PID untuk mendeteksi spoofing/impersonasi)
vol -f memory.dmp windows.pstree

# Menemukan proses siluman yang disembunyikan lewat teknik Direct Kernel Object Manipulation (DKOM)
vol -f memory.dmp windows.psscan
```

---

## 2. Investigasi Koneksi Jaringan & Soket

```bash
# Menampilkan seluruh koneksi TCP/UDP aktif beserta PID proses pemiliknya
vol -f memory.dmp windows.netscan
```

---

## 3. Deteksi Injeksi Kode & Malware Memory

```bash
# Mendeteksi DLL injection / reflective injection (halaman memori bertanda PAGE_EXECUTE_READWRITE)
vol -f memory.dmp windows.malfind

# Mengekstrak (dump) file atau memori proses tertentu berdasarkan PID
vol -f memory.dmp -o ./extracted_artifacts windows.dumpfiles --pid <PID>
```

---

## 4. Ekstraksi Kredensial & Hive Registry

```bash
# Mengekstrak hash password dari memory (SAM & SYSTEM hives)
vol -f memory.dmp windows.hashdump

# Memeriksa string command-line arguments yang dieksekusi setiap proses
vol -f memory.dmp windows.cmdline
```
