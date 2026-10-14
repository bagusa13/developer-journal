# 🧠 Volatile Memory Forensics Cheatsheet (Volatility 3)

Panduan praktis investigasi dump RAM (*volatile memory forensics*) menggunakan framework Volatility 3 untuk mendeteksi proses mencurigakan, rootkit, dan injeksi kode (*code injection*).

---

## 1. Identifikasi Proses & Hirarki
```bash
# Daftar proses aktif
vol -f memory.dmp windows.pslist

# Pohon proses (melihat parent-child PID untuk mendeteksi impersonasi)
vol -f memory.dmp windows.pstree

# Menemukan proses siluman yang disembunyikan lewat unlinking DKOM
vol -f memory.dmp windows.psscan
```

---

## 2. Investigasi Koneksi Jaringan & Soket
```bash
# Menampilkan koneksi TCP/UDP aktif beserta PID pemiliknya
vol -f memory.dmp windows.netscan
```

---

## 3. Deteksi Injeksi Kode & Malware Memory
```bash
# Mendeteksi DLL injection / reflective injection (halaman memori PAGE_EXECUTE_READWRITE)
vol -f memory.dmp windows.malfind

# Dump memory proses tertentu berdasarkan PID
vol -f memory.dmp -o output_dir windows.dumpfiles --pid <PID>
```
