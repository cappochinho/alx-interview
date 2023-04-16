#!/usr/bin/python3

import signal
import sys
from collections import defaultdict

overall_file_size = 0
status_code_count = defaultdict(int)
no_of_lines:int  = 0

for line in sys.stdin:
    line = line.strip()
    try:
        ip_addr, _, _, request, status_code, file_size = line.split(" ")
        if request != "GET /projects/260 HTTP/1.1":
            continue
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue

    overall_file_size += file_size
    status_code_count[status_code] += 1
    no_of_lines += 1

    if no_of_lines % 10 == 0 or KeyboardInterrupt:
        print(f"File size: {overall_file_size}")
        for status_code in sorted(status_code_count.keys()):
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                print(f"{status_code}: {status_code_count[status_code]}")

print(f"File size: {overall_file_size}")
for status_code in sorted(status_code_count.keys()):
    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
        print(f"{status_code}: {status_code_count[status_code]}")
