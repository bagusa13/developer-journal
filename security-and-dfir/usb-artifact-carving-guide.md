# Physical USB Digital Forensics & File Carving Guide

> **Author**: Mohammad Bagus Satrio ([@bagusa13](https://github.com/bagusa13))  
> **Related Project**: [dfir-usb-investigation](https://github.com/bagusa13/dfir-usb-investigation)  
> **Repository**: [developer-journal](https://github.com/bagusa13/developer-journal)

---

## 1. Overview & Chain of Custody

Dalam investigasi digital forensik perangkat penyimpanan eksternal (USB flash drive), integritas bukti (*evidence integrity*) harus dijaga menggunakan write-blocker perangkat keras atau akuisisi citra forensik bit-stream (format E01 / RAW DD).

---

## 2. Magic Numbers / File Signatures for Carving

Ketika tabel partisi (MBR/GPT) atau file allocation table (exFAT/FAT32) dirusak atau sengaja dihapus (*anti-forensics*), proses **file carving** dilakukan dengan memindai byte signature mentah:

| Format File | Header Hex Signature (Start of File) | Footer Hex Signature (End of File) |
| :--- | :--- | :--- |
| **JPEG** | `FF D8 FF E0` atau `FF D8 FF E1` | `FF D9` |
| **PNG** | `89 50 4E 47 0D 0A 1A 0A` | `49 45 4E 44 AE 42 60 82` |
| **PDF** | `25 50 44 46` (`%PDF-`) | `25 25 45 4F 46` (`%%EOF`) |
| **ZIP / DOCX** | `50 4B 03 04` (`PK..`) | `50 4B 05 06` |
| **SQLite DB** | `53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33 00` | N/A (Struktur berbasis page) |

---

## 3. exFAT & MBR Structure Anatomy

- **MBR Sector 0**: Berisi executable bootstrap code (446 bytes) + 4 Partition Table entries (64 bytes) + Magic signature `55 AA` (offset `0x1FE`).
- **exFAT VBR (Volume Boot Record)**: Berisi Jump Boot `EB 76 90`, OEM Name `EXFAT   `, Bytes Per Sector shift, dan Clusters Per Allocation Unit.
