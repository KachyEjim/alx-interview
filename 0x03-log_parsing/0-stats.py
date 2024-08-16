#!/usr/bin/python3
"""Script to parse log data and compute metrics."""

import sys
import re

# Dictionary to store the count of each status code
STATUS_CODE = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

regex = (
    r"^(\d{1,3}\.){3}\d{1,3}\s-\s\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\]"
    r'\s"GET /projects/\d+ HTTP/1\.1"\s(\d{3})\s(\d+)$'
)

# Initialize counters
count = 0
size = 0


def print_metrics():
    """Function to print the accumulated metrics."""
    print(f"File size: {size}")
    for status, value in sorted(STATUS_CODE.items()):
        if value > 0:
            print(f"{status}: {value}")


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            match = re.match(regex, line)
            if not match:
                continue

            status_code = match.group(2)
            file_size = match.group(3)

            size += int(file_size)

            if status_code in STATUS_CODE:
                STATUS_CODE[status_code] += 1

            count += 1

            if count == 10:
                print_metrics()
                count = 0

    except KeyboardInterrupt:
        print_metrics()
        raise
