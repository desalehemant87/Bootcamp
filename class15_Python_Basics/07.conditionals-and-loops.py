"""
Lab 2: Conditionals and Loops for DevOps
=========================================
Objective: Master if/elif/else, for loops, while loops, and list comprehensions

Topics Covered:
- Conditional statements (if/elif/else)
- For loops with ranges, lists, dictionaries
- While loops
- List comprehensions
- Break and continue statements
"""

# ========================================
# Exercise 1: Conditional Statements - Server Health Check
# ========================================
print("=" * 50)
print("Exercise 1: Conditional Statements")
print("=" * 50)

# TODO: Check server status
server_status = "running"

if server_status == "running":
    print("Server is healthy")
elif server_status == "stopped":
    print("Server is stopped - needs restart")
else:
    print("Unknown server status")

# TODO: Check CPU usage with multiple conditions
cpu_usage = 85

if cpu_usage < 50:
    print(f"CPU usage is normal: {cpu_usage}%")
elif cpu_usage >= 50 and cpu_usage < 80:
    print(f"CPU usage is elevated: {cpu_usage}%")
elif cpu_usage >= 80 and cpu_usage < 95:
    print(f"WARNING: CPU usage is high: {cpu_usage}%")
else:
    print(f"CRITICAL: CPU usage is critical: {cpu_usage}%")

# TODO: Check multiple conditions (memory AND disk)
memory_usage = 60
disk_usage = 90

if memory_usage > 80 and disk_usage > 80:
    print("ALERT: Both memory and disk are high!")
elif memory_usage > 80 or disk_usage > 80:
    if memory_usage > 80:
        print(f"WARNING: Memory usage is high: {memory_usage}%")
    if disk_usage > 80:
        print(f"WARNING: Disk usage is high: {disk_usage}%")
else:
    print("System resources are normal")

# TODO: Ternary operator for quick checks
environment = "production"
log_level = "ERROR" if environment == "production" else "DEBUG"
print(f"Log level for {environment}: {log_level}")

print()

# ========================================
# Exercise 2: For Loops - Iterating Through Infrastructure
# ========================================
print("=" * 50)
print("Exercise 2: For Loops")
print("=" * 50)

# TODO: Loop through list of servers
servers = ["web-1", "web-2", "db-1", "cache-1"]

print("Checking all servers:")
for server in servers:
    print(f"  Pinging {server}...")

# TODO: Loop with index using enumerate
print("\nServers with index:")
for index, server in enumerate(servers, start=1):
    print(f"  {index}. {server}")

# TODO: Loop through range
print("\nRestarting services (countdown):")
for i in range(5, 0, -1):
    print(f"  Restarting in {i}...")
print("  Service restarted!")

# TODO: Loop through dictionary
server_info = {
    "hostname": "web-server-1",
    "ip": "192.168.1.10",
    "port": 8080,
    "status": "running"
}

print("\nServer configuration:")
for key, value in server_info.items():
    print(f"  {key}: {value}")

# TODO: Nested loops - checking multiple servers with multiple services
infrastructure = {
    "web-1": ["nginx", "nodejs", "pm2"],
    "web-2": ["nginx", "nodejs", "pm2"],
    "db-1": ["postgresql", "redis"]
}

print("\nChecking services on all servers:")
for server, services in infrastructure.items():
    print(f"\n{server}:")
    for service in services:
        print(f"  - {service} is running")

print()

# ========================================
# Exercise 3: While Loops - Monitoring and Retries
# ========================================
print("=" * 50)
print("Exercise 3: While Loops")
print("=" * 50)

# TODO: Simple while loop with counter
retry_count = 0
max_retries = 3

print("Attempting to connect to server:")
while retry_count < max_retries:
    retry_count += 1
    print(f"  Attempt {retry_count}/{max_retries}")
    # Simulate connection attempt
    if retry_count == 2:  # Simulate success on 2nd attempt
        print("  Connection successful!")
        break
    else:
        # This executes if loop completes without break
        if retry_count >= max_retries:
            print("  Failed to connect after all retries")

# TODO: While loop with condition
print("\nMonitoring queue size:")
queue_size = 100
threshold = 10

while queue_size > threshold:
    print(f"  Queue size: {queue_size} - Processing...")
    queue_size -= 15  # Simulate processing

print(f"  Queue size: {queue_size} - Below threshold, monitoring stopped")

print()

# ========================================
# Exercise 4: Break and Continue Statements
# ========================================
print("=" * 50)
print("Exercise 4: Break and Continue")
print("=" * 50)

# TODO: Using break to exit loop early
servers_to_check = ["web-1", "web-2", "web-3", "db-1", "cache-1"]

print("Checking servers until error is found:")
for server in servers_to_check:
    if server == "web-3":
        print(f"  ERROR found on {server} - stopping checks")
        break
    print(f"  {server} - OK")

# TODO: Using continue to skip items
print("\nProcessing servers (skipping maintenance):")
server_statuses = {
    "web-1": "running",
    "web-2": "maintenance",
    "web-3": "running",
    "db-1": "maintenance",
    "cache-1": "running"
}

for server, status in server_statuses.items():
    if status == "maintenance":
        print(f"  {server} - Skipping (in maintenance)")
        continue
    print(f"  {server} - Processing...")

print()

# ========================================
# Exercise 5: List Comprehensions - Fast and Pythonic
# ========================================
print("=" * 50)
print("Exercise 5: List Comprehensions")
print("=" * 50)

# TODO: Basic list comprehension - generate server names
server_numbers = list(range(1, 6))
servers_list = [f"web-server-{i}" for i in server_numbers]
print(f"Generated servers: {servers_list}")

# TODO: List comprehension with condition - filter running servers
all_servers = [
    {"name": "web-1", "status": "running"},
    {"name": "web-2", "status": "stopped"},
    {"name": "web-3", "status": "running"},
    {"name": "db-1", "status": "running"}
]

running_servers = [server["name"] for server in all_servers if server["status"] == "running"]
print(f"Running servers: {running_servers}")

# TODO: Transform data with list comprehension
ports = [80, 443, 8080, 3000]
firewall_rules = [f"ALLOW TCP port {port}" for port in ports]
print(f"Firewall rules: {firewall_rules}")

# TODO: List comprehension with if-else
cpu_values = [45, 78, 92, 34, 88, 23]
cpu_status = ["HIGH" if cpu > 80 else "NORMAL" for cpu in cpu_values]
print(f"CPU values: {cpu_values}")
print(f"CPU status: {cpu_status}")

# TODO: Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# TODO: Dictionary comprehension
server_list = ["web-1", "web-2", "db-1"]
server_ports = {server: 8080 if "web" in server else 5432 for server in server_list}
print(f"Server ports: {server_ports}")

# TODO: Set comprehension - extract unique environments
deployments = ["prod-web-1", "staging-web-1", "prod-db-1", "dev-web-1", "staging-db-1"]
environments = {deploy.split("-")[0] for deploy in deployments}
print(f"Unique environments: {environments}")

print()

# ========================================
# Exercise 6: Real DevOps Scenario - Log Analysis
# ========================================
print("=" * 50)
print("Exercise 6: Real DevOps Scenario - Log Analysis")
print("=" * 50)

# Simulated log entries
log_entries = [
    "2024-01-15 10:23:45 INFO User login successful",
    "2024-01-15 10:24:12 ERROR Database connection failed",
    "2024-01-15 10:24:15 INFO Retrying database connection",
    "2024-01-15 10:24:18 ERROR Database connection failed",
    "2024-01-15 10:25:01 WARNING High memory usage detected",
    "2024-01-15 10:25:30 INFO User logout",
    "2024-01-15 10:26:00 ERROR API request timeout",
    "2024-01-15 10:26:15 INFO Cache cleared",
]

# TODO: Count errors
error_count = 0
warning_count = 0
info_count = 0

for log in log_entries:
    if "ERROR" in log:
        error_count += 1
    elif "WARNING" in log:
        warning_count += 1
    elif "INFO" in log:
        info_count += 1

print(f"Log Analysis:")
print(f"  INFO: {info_count}")
print(f"  WARNING: {warning_count}")
print(f"  ERROR: {error_count}")

# TODO: Extract and print only errors
print("\nError logs:")
error_logs = [log for log in log_entries if "ERROR" in log]
for error in error_logs:
    print(f"  {error}")

# TODO: Find critical patterns
print("\nDatabase issues:")
db_issues = [log for log in log_entries if "Database" in log]
for issue in db_issues:
    print(f"  {issue}")

print()

# ========================================
# Exercise 7: Deployment Automation Example
# ========================================
print("=" * 50)
print("Exercise 7: Deployment Automation")
print("=" * 50)

servers_to_deploy = ["web-1", "web-2", "web-3"]
deployment_steps = ["backup", "stop_service", "deploy", "start_service", "health_check"]

print("Starting deployment process:")
for server in servers_to_deploy:
    print(f"\nDeploying to {server}:")

    for step_num, step in enumerate(deployment_steps, start=1):
        print(f"  Step {step_num}/{len(deployment_steps)}: {step.replace('_', ' ').title()}", end="")

        # Simulate a failure on web-2 during deploy step
        if server == "web-2" and step == "deploy":
            print(" - FAILED")
            print(f"  Deployment failed on {server}, rolling back...")
            break
        else:
            print(" - OK")
    else:
        print(f"  Deployment to {server} completed successfully!")

print("\n" + "=" * 50)
print("Lab 2 Complete!")
print("=" * 50)