#!/usr/bin/python3
"""
0-stats module
"""
import sys


# Initialize variables
total_size = 0
status = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
}
line_count = 0


def print_stat(status, total_size):
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status.items()):
        if count != 0:
            print("{}: {}".format(status_code, count))


if __name__ == "__main__":
    try:
        # Read lines from stdin
        for line in sys.stdin:
            data = line.split()
            if len(data) > 4:
                stat = data[-2]
                if stat in status.keys():
                    status[stat] += 1
                total_size += int(data[-2])
                line_count += 1
            if line_count == 10:
                line_count = 0
                print_stat(status, total_size)
    except Exception:
        pass
    finally:
        print_stat(status, total_size)
