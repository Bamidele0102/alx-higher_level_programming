#!/usr/bin/python3
import sys
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)

try:
    for i, line in enumerate(sys.stdin, start=1):
        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            total_file_size += file_size
            status_code_counts[status_code] += 1

            if i % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_code_counts):
                    print(f"{code}: {status_code_counts[code]}")

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")
    sys.exit(0)
