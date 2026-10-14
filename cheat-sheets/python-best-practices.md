# Python Scripting & Clean Architecture Cheatsheet

> **Author**: Mohammad Bagus Satrio ([@bagusa13](https://github.com/bagusa13))  
> **Repository**: [developer-journal](https://github.com/bagusa13/developer-journal)

Panduan standar dan praktik terbaik dalam menulis script Python yang modular, mudah di-maintain, andal (*fault-tolerant*), dan berstandar produksi.

---

## 1. Type Hinting & Anotasi Statis

Gunakan module `typing` untuk memperjelas ekspektasi tipe data masukan dan luaran fungsi.

```python
from typing import List, Dict, Optional, Tuple, Union
from pathlib import Path

def parse_config(file_path: Path, strict_mode: bool = False) -> Dict[str, Union[str, int]]:
    """Membaca konfigurasi dan mengembalikan dictionary hasil parse."""
    if not file_path.is_file():
        if strict_mode:
            raise FileNotFoundError(f"Configuration file missing: {file_path}")
        return {}
    # Logika parsing...
    return {"host": "127.0.0.1", "port": 8080}
```

---

## 2. Manipulasi Path Modern (`pathlib`)

Hindari konkatenasi string manual atau `os.path.join`. Gunakan `pathlib.Path`:

```python
from pathlib import Path

# Inisialisasi direktori kerja
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CONFIG_FILE = BASE_DIR / "config" / "settings.json"

# Operasi umum
DATA_DIR.mkdir(parents=True, exist_ok=True)  # Buat direktori jika belum ada
if CONFIG_FILE.exists():
    raw_content = CONFIG_FILE.read_text(encoding="utf-8")
```

---

## 3. Manajemen Resource dengan Context Managers (`with`)

Pastikan seluruh resource (file descriptor, database connection, socket) tertutup otomatis meskipun terjadi error runtime:

```python
# Membaca file berukuran besar secara chunk (hemat memori)
CHUNK_SIZE = 64 * 1024  # 64 KB

with open("evidence.bin", "rb") as stream:
    while chunk := stream.read(CHUNK_SIZE):
        # Proses chunk tanpa memuat seluruh file ke RAM
        pass
```

---

## 4. Logging Terstruktur vs `print()`

Haram menggunakan `print()` untuk debugging di script produksi. Gunakan module `logging`:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)-7s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

logger.info("Script started successfully.")
logger.warning("Resource utilization exceeds 80%.")
logger.error("Failed to connect to database host.", exc_info=True)
```

---

## 5. Hierarki Penanganan Eksepsi (*Exception Handling*)

Tangkap error spesifik, jangan pernah menggunakan `except Exception:` secara buta tanpa mencatat log error:

```python
import sys

try:
    with open("critical_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    logger.error("Critical file not found. Falling back to default settings.")
    data = {}
except json.JSONDecodeError as err:
    logger.critical(f"Malformed JSON syntax on line {err.lineno}: {err.msg}")
    sys.exit(1)
```

---

## 6. Standar Exit Codes (Unix Convention)

| Exit Code | Makna / Konvensi |
| :--- | :--- |
| `0` | **Success** (Eksekusi berhasil tanpa galat) |
| `1` | **General Error** (Kesalahan runtime umum / file tidak ditemukan) |
| `2` | **Misuse of Shell Builtins** (Parameter CLI salah / argumen wajib kurang) |
| `126` | Perintah yang dipanggil tidak memiliki izin eksekusi (*permission denied*) |
| `127` | Perintah atau binary yang dipanggil tidak ditemukan (*command not found*) |
| `130` | Dihentikan oleh sinyal pengguna via `Ctrl+C` (*SIGINT*) |
