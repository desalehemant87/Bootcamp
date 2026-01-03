"""
Lab 6: String Manipulation and Formatting
==========================================
Objective: Master string operations for log parsing, text processing, and formatting

Topics Covered:
- String methods (split, join, replace, strip, etc.)
- String formatting (f-strings, format(), %)
- String searching and matching
- Regular expressions basics
- Multi-line strings
- String parsing for logs and configs
"""

import re
from datetime import datetime

# ========================================
# Exercise 1: Basic String Operations
# ========================================
print("=" * 50)
print("Exercise 1: Basic String Operations")
print("=" * 50)

# TODO: String basics
server_name = "  web-server-01  "
print(f"Original: '{server_name}'")

# Remove whitespace
clean_name = server_name.strip()
print(f"Stripped: '{clean_name}'")

# Case conversion
print(f"Upper: {clean_name.upper()}")
print(f"Lower: {clean_name.lower()}")
print(f"Title: {clean_name.title()}")

# Replace
new_name = clean_name.replace("web", "api")
print(f"Replaced: {new_name}")

# Check content
print(f"\nContains 'web': {clean_name.find('web') != -1}")
print(f"Starts with 'web': {clean_name.startswith('web')}")
print(f"Ends with '01': {clean_name.endswith('01')}")

print()

# ========================================
# Exercise 2: Splitting and Joining
# ========================================
print("=" * 50)
print("Exercise 2: Splitting and Joining Strings")
print("=" * 50)

# TODO: Split by delimiter
log_entry = "2024-01-15 10:23:45 ERROR Database connection failed"
parts = log_entry.split()
print(f"Original: {log_entry}")
print(f"Split by space: {parts}")

# Specific delimiter
csv_line = "web-server-01,192.168.1.10,running,4,16"
fields = csv_line.split(",")
print(f"\nCSV: {csv_line}")
print(f"Fields: {fields}")

# Unpack values
hostname, ip, status, cpu, memory = csv_line.split(",")
print(f"  Hostname: {hostname}")
print(f"  IP: {ip}")
print(f"  Status: {status}")

# TODO: Join strings
servers = ["web-1", "web-2", "db-1", "cache-1"]
print(f"\nServer list: {servers}")
print(f"Joined with comma: {', '.join(servers)}")
print(f"Joined with newline:\n{chr(10).join(servers)}")

# TODO: Split lines
multi_line = """server1: running
server2: stopped
server3: running"""

lines = multi_line.split("\n")
print(f"\nMulti-line text split into {len(lines)} lines:")
for line in lines:
    print(f"  {line}")

print()

# ========================================
# Exercise 3: String Formatting
# ========================================
print("=" * 50)
print("Exercise 3: String Formatting")
print("=" * 50)

# TODO: f-strings (Python 3.6+)
server = "web-server-01"
cpu_usage = 75.5
memory_usage = 82.3

print("f-string formatting:")
print(f"Server {server} - CPU: {cpu_usage}%, Memory: {memory_usage}%")
print(f"CPU: {cpu_usage:6.2f}%")  # Width 6, 2 decimals
print(f"Memory: {memory_usage:>8.1f}%")  # Right aligned, width 8

# TODO: format() method
print("\nformat() method:")
message = "Server {} has {}% CPU usage".format(server, cpu_usage)
print(message)

message = "Server {name} at {ip} is {status}".format(
    name="web-1",
    ip="192.168.1.10",
    status="running"
)
print(message)

# TODO: Old-style % formatting (still used in some codebases)
print("\nOld-style % formatting:")
print("Server %s has %.1f%% CPU usage" % (server, cpu_usage))

# TODO: Number formatting
value = 1234567.89
print(f"\nNumber formatting:")
print(f"Default: {value}")
print(f"With commas: {value:,}")
print(f"Two decimals: {value:.2f}")
print(f"Scientific: {value:e}")

# TODO: Padding and alignment
print(f"\nAlignment:")
print(f"{'Left':<10} | {'Center':^10} | {'Right':>10}")
print(f"{'---':<10} | {'---':^10} | {'---':>10}")
print(f"{'Value':<10} | {'123':^10} | {'999':>10}")

print()

# ========================================
# Exercise 4: Multi-line Strings and Templates
# ========================================
print("=" * 50)
print("Exercise 4: Multi-line Strings")
print("=" * 50)

# TODO: Triple-quoted strings
config_template = """
# Server Configuration
server_name = {hostname}
ip_address = {ip}
port = {port}
environment = {env}

# Database Settings
db_host = {db_host}
db_port = {db_port}
"""

config = config_template.format(
    hostname="web-server-01",
    ip="192.168.1.10",
    port=8080,
    env="production",
    db_host="db.example.com",
    db_port=5432
)

print("Generated configuration:")
print(config)

# TODO: Multi-line with line continuation
long_command = (
    "docker run -d "
    "--name myapp "
    "--port 8080:8080 "
    "--env DB_HOST=localhost "
    "myapp:latest"
)
print(f"Long command:\n{long_command}")

print()

# ========================================
# Exercise 5: String Searching and Matching
# ========================================
print("=" * 50)
print("Exercise 5: String Searching")
print("=" * 50)

log_line = "2024-01-15 10:23:45 ERROR [database] Connection timeout after 30s"

# TODO: Find and index
print(f"Log: {log_line}")
print(f"\nFind 'ERROR': position {log_line.find('ERROR')}")
print(f"Find 'WARNING': position {log_line.find('WARNING')}")  # -1 if not found

# Count occurrences
text = "server server server database server"
print(f"\nText: {text}")
print(f"Count 'server': {text.count('server')}")

# Check if substring exists
if "ERROR" in log_line:
    print("\nLog contains ERROR")

if "database" in log_line.lower():
    print("Log is related to database")

print()

# ========================================
# Exercise 6: Regular Expressions
# ========================================
print("=" * 50)
print("Exercise 6: Regular Expressions")
print("=" * 50)

# TODO: Match IP addresses
log_with_ip = "Connection from 192.168.1.100 failed"
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

match = re.search(ip_pattern, log_with_ip)
if match:
    print(f"Found IP address: {match.group()}")

# TODO: Find all matches
log_text = """
2024-01-15 10:23:45 Connection from 192.168.1.100
2024-01-15 10:24:12 Connection from 10.0.0.50
2024-01-15 10:25:01 Connection from 172.16.0.25
"""

ip_addresses = re.findall(ip_pattern, log_text)
print(f"\nFound IP addresses: {ip_addresses}")

# TODO: Extract log level
log_entries = [
    "2024-01-15 10:23:45 INFO User logged in",
    "2024-01-15 10:24:12 ERROR Database connection failed",
    "2024-01-15 10:25:01 WARNING High memory usage",
    "2024-01-15 10:26:15 DEBUG Processing request",
]

log_level_pattern = r'(INFO|ERROR|WARNING|DEBUG)'

print("\nExtracting log levels:")
for entry in log_entries:
    match = re.search(log_level_pattern, entry)
    if match:
        level = match.group(1)
        print(f"  {level}: {entry}")

# TODO: Replace with regex
text = "Server web-server-01 and web-server-02 are running"
pattern = r'web-server-\d+'
replacement = "api-server"
new_text = re.sub(pattern, replacement, text)
print(f"\nOriginal: {text}")
print(f"Replaced: {new_text}")

print()

# ========================================
# Exercise 7: Log Parsing
# ========================================
print("=" * 50)
print("Exercise 7: Real DevOps Scenario - Log Parsing")
print("=" * 50)

# Sample log entries
logs = """
2024-01-15 10:23:45 INFO [web-server-01] Request processed in 45ms
2024-01-15 10:24:12 ERROR [web-server-02] Database connection timeout
2024-01-15 10:24:15 INFO [web-server-01] Request processed in 32ms
2024-01-15 10:25:01 WARNING [cache-server] Memory usage at 85%
2024-01-15 10:25:30 ERROR [web-server-02] Failed to connect to Redis
2024-01-15 10:26:00 INFO [web-server-01] Request processed in 28ms
"""

# TODO: Parse log entries
log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) \[([^\]]+)\] (.+)'

parsed_logs = []
for line in logs.strip().split('\n'):
    match = re.match(log_pattern, line)
    if match:
        timestamp, level, server, message = match.groups()
        parsed_logs.append({
            'timestamp': timestamp,
            'level': level,
            'server': server,
            'message': message
        })

print("Parsed logs:")
for log in parsed_logs:
    print(f"  {log['timestamp']} | {log['level']:7} | {log['server']:15} | {log['message']}")

# TODO: Analyze logs
error_count = sum(1 for log in parsed_logs if log['level'] == 'ERROR')
warning_count = sum(1 for log in parsed_logs if log['level'] == 'WARNING')
servers_with_errors = set(log['server'] for log in parsed_logs if log['level'] == 'ERROR')

print(f"\nLog Analysis:")
print(f"  Total entries: {len(parsed_logs)}")
print(f"  Errors: {error_count}")
print(f"  Warnings: {warning_count}")
print(f"  Servers with errors: {', '.join(servers_with_errors)}")

print()

# ========================================
# Exercise 8: Configuration File Parsing
# ========================================
print("=" * 50)
print("Exercise 8: Configuration File Parsing")
print("=" * 50)

config_file = """
# Application Configuration
APP_NAME=my-web-app
APP_ENV=production
APP_PORT=8080

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp_db
DB_USER=admin

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
"""

# TODO: Parse key=value pairs
config = {}
for line in config_file.split('\n'):
    line = line.strip()

    # Skip empty lines and comments
    if not line or line.startswith('#'):
        continue

    # Parse key=value
    if '=' in line:
        key, value = line.split('=', 1)
        config[key.strip()] = value.strip()

print("Parsed configuration:")
for key, value in sorted(config.items()):
    print(f"  {key} = {value}")

# TODO: Group by prefix
print("\nGrouped by category:")
db_config = {k: v for k, v in config.items() if k.startswith('DB_')}
redis_config = {k: v for k, v in config.items() if k.startswith('REDIS_')}

print("\nDatabase config:")
for key, value in db_config.items():
    print(f"  {key} = {value}")

print("\nRedis config:")
for key, value in redis_config.items():
    print(f"  {key} = {value}")

print()

# ========================================
# Exercise 9: URL and Path Manipulation
# ========================================
print("=" * 50)
print("Exercise 9: URL and Path Processing")
print("=" * 50)

# TODO: Extract components from URL
url = "https://api.example.com:8080/v1/users/123?active=true&limit=10"

print(f"URL: {url}")

# Extract protocol
protocol = url.split("://")[0]
print(f"  Protocol: {protocol}")

# Extract domain and path
rest = url.split("://")[1]
if "?" in rest:
    path_part, query_part = rest.split("?", 1)
else:
    path_part = rest
    query_part = ""

if "/" in path_part:
    domain_part, path = path_part.split("/", 1)
    path = "/" + path
else:
    domain_part = path_part
    path = "/"

print(f"  Domain: {domain_part}")
print(f"  Path: {path}")

# Parse query parameters
if query_part:
    params = {}
    for param in query_part.split("&"):
        key, value = param.split("=")
        params[key] = value
    print(f"  Query params: {params}")

print()

# ========================================
# Exercise 10: Text Cleanup and Normalization
# ========================================
print("=" * 50)
print("Exercise 10: Text Cleanup")
print("=" * 50)

# TODO: Clean messy input
messy_server_names = [
    "  Web-Server-01  ",
    "WEB-SERVER-02",
    "web_server_03",
    "  DB-SERVER-01\n",
    "Cache Server 01"
]

print("Original server names:")
for name in messy_server_names:
    print(f"  '{name}'")

# Clean and normalize
clean_names = []
for name in messy_server_names:
    # Strip whitespace
    clean = name.strip()
    # Convert to lowercase
    clean = clean.lower()
    # Replace spaces and underscores with hyphens
    clean = clean.replace(" ", "-").replace("_", "-")
    clean_names.append(clean)

print("\nCleaned server names:")
for name in clean_names:
    print(f"  {name}")

print()

# ========================================
# Exercise 11: Building Reports
# ========================================
print("=" * 50)
print("Exercise 11: Building Formatted Reports")
print("=" * 50)

# Server data
servers = [
    {"name": "web-01", "cpu": 45.2, "memory": 62.5, "disk": 78.3, "status": "UP"},
    {"name": "web-02", "cpu": 78.9, "memory": 85.2, "disk": 45.6, "status": "UP"},
    {"name": "db-01", "cpu": 92.1, "memory": 91.8, "disk": 88.5, "status": "WARNING"},
    {"name": "cache-01", "cpu": 34.5, "memory": 45.2, "disk": 23.1, "status": "UP"},
]

# Build report
report = []
report.append("=" * 70)
report.append("SERVER HEALTH REPORT")
report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report.append("=" * 70)
report.append("")

# Header
report.append(f"{'Server':<12} | {'CPU %':>8} | {'Memory %':>8} | {'Disk %':>8} | {'Status':<10}")
report.append("-" * 70)

# Data rows
for server in servers:
    line = (
        f"{server['name']:<12} | "
        f"{server['cpu']:>8.1f} | "
        f"{server['memory']:>8.1f} | "
        f"{server['disk']:>8.1f} | "
        f"{server['status']:<10}"
    )
    report.append(line)

report.append("=" * 70)

# Print report
print("\n".join(report))

print("\n" + "=" * 50)
print("Lab 6 Complete!")
print("=" * 50)

# ========================================
# Your Tasks:
# ========================================
"""
1. Write code to extract email addresses from a text using regex

2. Parse a log file and count occurrences of each log level (INFO, ERROR, WARNING, DEBUG)

3. Create a function that validates if a string is a valid IP address

4. Write code to parse a CSV line and handle quoted fields that contain commas

5. Build a function that formats file sizes (bytes) into human-readable format (KB, MB, GB)

6. Create a script that parses nginx access logs and extracts:
   - IP addresses
   - HTTP methods
   - Status codes
   - Response times

7. Write a function that generates a formatted table from a list of dictionaries

8. Parse a multiline string containing server metrics and calculate averages

9. Create a URL builder function that properly encodes query parameters

10. Build a log filter that:
    - Reads log entries
    - Filters by date range
    - Filters by log level
    - Filters by server name
    - Outputs matching entries
"""