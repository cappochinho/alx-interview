#!/usr/bin/python3

import sys
from collections import defaultdict

# initialize variables and data structures
total_size = 0
status_codes = defaultdict(int)
line_count = 0

try:
    # read input line by line
    for line in sys.stdin:
        # split line into components
        try:
            ip_address, _, date, request, status_code, file_size = line.split()
            if request != "GET /projects/260 HTTP/1.1":
                continue
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # update metrics
        total_size += file_size
        status_codes[status_code] += 1
        line_count += 1

        # print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes):
                print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    # print statistics on keyboard interruption
    print(f"\nTotal file size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")
