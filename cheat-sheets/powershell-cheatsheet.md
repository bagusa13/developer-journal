# PowerShell Systems Automation Cheatsheet

> **Author**: Mohammad Bagus Satrio ([@bagusa13](https://github.com/bagusa13))  
> **Repository**: [developer-journal](https://github.com/bagusa13/developer-journal)

Pedoman administrasi sistem Windows, manajemen proses, dan otomasi pipeline PowerShell berbasis objek (*Object-Oriented Pipeline*).

---

## 1. Pipeline & Manipulasi Objek

Berbeda dengan Bash yang memproses stream teks, PowerShell mengalirkan objek nyata:

```powershell
# Filter proses yang menggunakan RAM > 100 MB
Get-Process | Where-Object WorkingSet64 -gt 100MB | Select-Object ProcessName, Id, @{Name="RAM_MB"; Expression={[math]::Round($_.WorkingSet64 / 1MB, 2)}} | Sort-Object RAM_MB -Descending

# Menghitung SHA-256 semua executable dalam sebuah folder
Get-ChildItem -Path "C:\Tools" -Filter *.exe -Recurse | Get-FileHash -Algorithm SHA256 | Select-Object Path, Hash
```

---

## 2. Inspeksi Port & Koneksi Jaringan (Triage)

```powershell
# Melihat seluruh koneksi TCP yang sedang berstatus LISTEN atau ESTABLISHED
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess | Sort-Object LocalPort

# Melakukan query test koneksi port spesifik (pengganti telnet/nc)
Test-NetConnection -ComputerName "1.1.1.1" -Port 53
```

---

## 3. Ekspor & Konversi Data (JSON, CSV, Clixml)

```powershell
# Mengambil data sistem dan menyimpan ke JSON terformat rapi
$systemInfo = [PSCustomObject]@{
    ComputerName = $env:COMPUTERNAME
    OSVersion    = (Get-CimInstance Win32_OperatingSystem).Caption
    Uptime       = (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
    ActiveUsers  = (Get-CimInstance Win32_ComputerSystem).UserName
}

$systemInfo | ConvertTo-Json -Depth 3 | Set-Content -Path "system_triage.json" -Encoding UTF8
```

---

## 4. Query WMI & CIM (Hardware & Services Audit)

```powershell
# Audit layanan Windows yang berjalan secara otomatis
Get-CimInstance Win32_Service | Where-Object { $_.StartMode -eq "Auto" -and $_.State -ne "Running" } | Select-Object Name, DisplayName, State

# Cek daftar USB drive yang terhubung ke sistem
Get-CimInstance Win32_DiskDrive | Where-Object InterfaceType -eq "USB" | Select-Object Model, DeviceID, Size, Partitions
```
