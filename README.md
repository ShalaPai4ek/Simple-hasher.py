# Simple-hasher.py
A simple file hasher that outputs the hash sum of a specified file to the terminal and compares it against a hash stored in a TXT file.

## Usage
hasher.py [-h] [-c TXT_FILE] [-a ALGORYTHM] [-s SIZE] path

positional arguments:
  path                  File path

options:
  -h, --help            show this help message and exit
  -c, --check TXT_FILE  Path to TXT file with hash code
  -a, --algorythm ALGORYTHM
                        Hash algorythm (by default: sha256)
  -s, --size SIZE       Chunk size in bites (by default: 65536)
