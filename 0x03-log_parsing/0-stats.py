#!/usr/bin/python3
"""
Parse a log line and return the status code and file size if valid.
"""
import sys

def parse_line(line):
    try:
        parts = line.split()
        if len(parts) < 6:
            return None, 0

        status_code = int(parts[-2])
        file_size = int(parts[-1])

        return status_code, file_size
    except (IndexError, ValueError):
        return None, 0

def print_metrics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)

            if status_code is not None:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
