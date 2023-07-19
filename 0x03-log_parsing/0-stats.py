#!/usr/bin/python3
"""
0-stats module
"""
import sys
import signal


# Initialize variables
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count != 0:
            print("{}: {}".format(status_code, count))

def process_line(line):
    global total_size, status_code_counts, line_count
    
    line_count += 1
    
    # Split line by space
    parts = line.split(" ")
    
    # Check if the line matches the expected format
    if len(parts) != 7:
        return
    
    # Extract status code and file size
    try:
        status_code = int(parts[5])
        file_size = int(parts[6])
    except ValueError:
        return
    
    # Update total file size
    total_size += file_size
    
    # Update status code counts
    if status_code in status_code_counts:
        status_code_counts[status_code] += 1

# Handle SIGINT (Ctrl+C) to print statistics and exit gracefully
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Set the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin
for line in sys.stdin:
    line = line.strip()
    
    # Process the line
    process_line(line)
    
    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_statistics()

# Print final statistics
print_statistics()

