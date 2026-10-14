# 🌐 Network Traffic Analysis & Wireshark Filter Cheatsheet

Daftar filter penting (*display filters*) untuk analisis paket jaringan dalam skenario investigasi insiden (*Incident Response*).

---

## 1. Analisis DNS Anomali & Tunneling
```wireshark
# Tampilkan seluruh query DNS yang dikirim
dns.flags.response == 0

# Deteksi query TXT mencurigakan (sering digunakan DNS C2 tunneling)
dns.qry.type == 16

# Filter domain tertentu
dns.qry.name contains "malicious-domain.com"
```

---

## 2. Investigasi HTTP & Web Payload
```wireshark
# Mencari seluruh request HTTP method POST (biasanya upload payload atau submit kredensial)
http.request.method == "POST"

# Mencari file yang diunduh via HTTP
http.response.code == 200 and http.content_type contains "application"

# Cari kata sandi dalam lalu lintas HTTP plain-text
frame contains "password" or frame contains "passwd" or frame contains "login"
```

---

## 3. Deteksi Pemindaian Jaringan (Port Scanning)
```wireshark
# Deteksi paket TCP SYN tanpa ACK (indikasi SYN stealth scan)
tcp.flags.syn == 1 and tcp.flags.ack == 0

# Deteksi paket TCP RST (koneksi ditolak oleh host target)
tcp.flags.reset == 1
```
