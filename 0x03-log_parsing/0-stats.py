#!/usr/bin/python3
"""Python file"""
import sys
import re

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
count = 0
size = 0


def print_func():
    """Print function"""
    print(f"File size: {size}")
    for status, value in STATUS_CODE.items():
        if value:
            print(f"{status}: {value}")


print("here")
if __name__ == "__main__":
    try:
        for line in sys.stdin:
            count += 1
            match = re.match(regex, line)
            if not re.match(regex, line):
                continue
            file_size = match.group(3)
            status_code = match.group(2)
            size += int(file_size)

            if status_code in STATUS_CODE.keys():
                STATUS_CODE[status_code] += 1
                if count == 10:
                    print_func()
                    count = 0

    except KeyboardInterrupt:
        print_func()
        count = 0
