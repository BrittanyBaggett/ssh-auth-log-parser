import re

# Regex pattern to extract timestamps, event types, usernames,
# source/destination IPs, ports, and authentication attempt counts
pattern = re.compile(
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(\w+) user=(\w+) "
    r"src_ip=(\d+\.\d+\.\d+\.\d+) "
    r"dst_ip=(\d+\.\d+\.\d+\.\d+) "
    r"port=(\d+) attempts=(\d+)"
)

# Open the log file and process each entry individually
with open("logs.txt", "r", encoding="utf-8") as file:
    for line in file:
        match = pattern.search(line)

        # Process the log entry only if it matches the expected format
        if match:
            # Convert authentication attempts to an integer
            attempts = int(match.group(7))

            # Display events exceeding the authentication attempt threshold
            if attempts > 3:
                print("Timestamp:", match.group(1))
                print("Reason:", match.group(2))
                print("User:", match.group(3))
                print("Source IP:", match.group(4))
                print("Destination IP:", match.group(5))
                print("Port:", match.group(6))
                print("Attempts:", attempts)
                print("_____________")
