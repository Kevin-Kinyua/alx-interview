#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics
"""
import sys


file_size = 0
total_file_sizes = 0
count_lines = 0

status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        data = line.split(" ")
        if len(data) > 4:
            arg = data[-2]
            file_size = int(data[-1])
            if arg in status_code.keys():
                status_code[arg] += 1
            total_file_sizes += file_size
            count_lines += 1
        if count_lines == 10:
            count_lines = 0
            print("File size: {}".format(total_file_sizes))
            for key, value in sorted(status_code.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_file_sizes))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))