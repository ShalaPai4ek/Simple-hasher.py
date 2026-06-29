# Simple-hasher.py

A lightweight command-line tool written in Python to calculate the cryptographic hash sum of a specified file and easily verify it against a hash stored in a text file.

---

## Installation

The recommended way to install this script as a system-wide CLI tool is using **pipx**, which isolates the application and prevents system package conflicts.

### Linux based distros
```bash
pipx install git+https://github.com/ShalaPai4ek/Simple-hasher.py
```

---

## Usage

```text
simple-hasher [-h] [-c TXT_FILE] [-a ALGORITHM] [-s SIZE] path
```

### Arguments & Options

| `path` | **Required.** File path |
| `-h, --help` | Show the help message and exit |
| `-c, --check TXT_FILE` | Path to a TXT file with hash code |
| `-a, --algorithm ALGORITHM` | Hashing algorithm (by default: sha256) |
| `-s, --size SIZE` | Chunk size in bites (by default: 65536) |
