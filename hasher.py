#!/usr/bin/env python3
import hashlib
import argparse
import sys
import os

def calculate_hash(path_file, algo='sha256', chunk=65536):
    if not os.path.exists(path_file):
        print(f"No such file or directory: '{path_file}'", file=sys.stderr)
        sys.exit(1)

    h = hashlib.new(algo)

    with open(path_file, 'rb') as f:
        while ch := f.read(chunk):
            h.update(ch)

    return h.hexdigest()

def compare_hash(path_file, path_hash, algo='sha256', chunk=65536):
    if not os.path.exists(path_file):
        print(f"No such file or directory: '{path_file}'", file=sys.stderr)
        sys.exit(1)
    elif not os.path.exists(path_hash):
        print(f"No such file or directory: '{path_hash}'", file=sys.stderr)
        sys.exit(1)

    with open(path_hash, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        expected_hash = content.split()[0].lower() #sha256sum
    
    actual_hash = calculate_hash(path_file, algo, chunk).lower()

    if actual_hash == expected_hash:
        print("The hash sums matches! :3")
        return True
    else:
        print("The hash sums do not match... :(")
        return False

def main():
    parser = argparse.ArgumentParser(description="Simple hasher on python")

    parser.add_argument('path', type=str, help="File path")

    parser.add_argument(
            '-c', '--check',
            type=str,
            metavar="TXT_FILE",
            help="Path to TXT file with hash code"
            )
    parser.add_argument(
            '-a', '--algorythm',
            type=str,
            default='sha256',
            help="Hash algorythm (by default: sha256)"
            )
    parser.add_argument(
            '-s', '--size',
            type=int,
            default=65536,
            help="Chunk size in bites (by default: 65536)"
            )
   
    args = parser.parse_args()
    
    if args.check:
        success = compare_hash(
                path_file=args.path,
                path_hash=args.check,
                algo=args.algorythm,
                chunk=args.size
                )
        if not success:
            sys.exit(1)
    else:
        result = calculate_hash(
                path_file=args.path,
                algo=args.algorythm,
                chunk=args.size
                )
        print(result)
    
if __name__ == "__main__":
    main()

