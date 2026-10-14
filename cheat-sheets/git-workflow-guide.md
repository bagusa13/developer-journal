# Git Workflow & Conventional Commits Playbook

> **Author**: Mohammad Bagus Satrio ([@bagusa13](https://github.com/bagusa13))  
> **Repository**: [developer-journal](https://github.com/bagusa13/developer-journal)

Pedoman manajemen version control, konvensi pesan commit standar industri (*Conventional Commits*), dan teknik rebase/recovery.

---

## 1. Standar Conventional Commits

Format commit terstruktur: `<type>(<scope>): <description>`

| Type | Kapan Digunakan | Contoh Pesan |
| :--- | :--- | :--- |
| `feat` | Menambahkan fitur atau script baru | `feat(hasher): add multi-threaded hashing support` |
| `fix` | Memperbaiki bug atau kesalahan logika | `fix(triage): resolve socket timeout on closed ports` |
| `docs` | Perubahan dokumentasi, README, panduan | `docs: update volatility 3 memory cheatsheet` |
| `refactor` | Perubahan struktur kode tanpa mengubah fungsi | `refactor(cli): simplify argument parsing logic` |
| `perf` | Optimasi performa dan efisiensi memori | `perf(io): increase stream read buffer to 64KB` |
| `test` | Menambahkan unit test atau data fixture | `test: add regression test cases for regex extractor` |
| `chore` | Pemeliharaan repo, dependensi, config | `chore: update requirements.txt dependencies` |

---

## 2. Operasi Esensial Branching & Stashing

```bash
# Membuat dan beralih ke branch fitur baru
git checkout -b feat/custom-parser

# Menyimpan perubahan sementara tanpa commit
git stash save "WIP: working on socket buffer"

# Mengembalikan perubahan yang di-stash
git stash pop

# Melihat histori commit ringkas satu baris
git log --oneline --graph --decorate -n 10
```

---

## 3. Merapikan Riwayat Commit (Interactive Rebase)

```bash
# Squash atau reword 3 commit terakhir sebelum push
git rebase -i HEAD~3

# Dalam editor rebase:
# pick -> gunakan commit tersebut
# squash (atau s) -> gabungkan ke commit sebelumnya
# reword (atau r) -> ubah pesan commit
```

---

## 4. Penyelamatan & Pembatalan Galat (Emergency Recovery)

```bash
# Membatalkan commit terakhir tapi mempertahankan perubahan file di working tree
git reset --soft HEAD~1

# Mencari commit yang hilang atau terhapus secara tidak sengaja
git reflog

# Mengembalikan commit tertentu dari riwayat reflog
git cherry-pick <commit-hash>
```
