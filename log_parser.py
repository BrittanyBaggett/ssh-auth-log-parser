import re

# Sample SSH authentication logs used for testing
logs = [
    "2026-11-03 08:45:22 SSH_AUTH_FAILURE user=jsmith src_ip=10.20.30.45 dst_ip=192.168.1.100 port=22 attempts=5",
    "2026-11-03 08:46:10 SSH_AUTH_SUCCESS user=admin src_ip=10.20.30.45 dst_ip=192.168.1.100 port=22 attempts=1",
    "2026-11-03 09:12:33 SSH_AUTH_FAILURE user=root src_ip=172.16.5.20 dst_ip=192.168.1.101 port=22 attempts=12"
]

# Regex pattern to extract timestamps, event types, usernames,
# source/destination IPs, ports, and authentication attempt counts
pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) user=(\w+) src_ip=(\d+\.\d+\.\d+\.\d+) dst_ip=(\d+\.\d+\.\d+\.\d+) port=(\d+) attempts=(\d+)")

# Iterate through each log entry and search for matching fields
for log in logs:
     # Convert attempts to an integer for numerical comparison
  match = re.search(pattern, log)
  if match:
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
