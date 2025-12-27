"""
Lab 8: Writing Clean, Reusable Functions
=========================================
Objective: Write modular, maintainable, and reusable functions

Topics Covered:
- Function basics (parameters, return values)
- Default arguments
- *args and **kwargs
- Type hints
- Docstrings
- Lambda functions
- Function composition
- Decorators
- Best practices
"""

import time
from typing import List, Dict, Optional, Union
from functools import wraps

# ========================================
# Exercise 1: Basic Functions
# ========================================
print("=" * 50)
print("Exercise 1: Basic Function Definition")
print("=" * 50)

# TODO: Simple function
def greet_server(server_name):
    """Greet a server by name"""
    return f"Hello, {server_name}!"

print(greet_server("web-server-01"))

# TODO: Function with multiple parameters
def check_resource(resource_name, threshold, current_value):
    """Check if resource usage exceeds threshold"""
    if current_value > threshold:
        return f"WARNING: {resource_name} at {current_value}% (threshold: {threshold}%)"
    else:
        return f"OK: {resource_name} at {current_value}%"

print(check_resource("CPU", 80, 75))
print(check_resource("Memory", 80, 92))

# TODO: Function with multiple return values
def get_server_stats(server_name):
    """Get server statistics (simulated)"""
    # Simulated data
    cpu = 75.5
    memory = 82.3
    disk = 45.2
    return cpu, memory, disk

cpu, memory, disk = get_server_stats("web-1")
print(f"\nServer stats: CPU={cpu}%, Memory={memory}%, Disk={disk}%")

print()

# ========================================
# Exercise 2: Default Arguments
# ========================================
print("=" * 50)
print("Exercise 2: Default Arguments")
print("=" * 50)

def deploy_app(app_name, environment="staging", replicas=1, timeout=300):
    """Deploy application with default values"""
    return {
        "app": app_name,
        "environment": environment,
        "replicas": replicas,
        "timeout": timeout
    }

# Using defaults
print("With defaults:", deploy_app("myapp"))

# Override some defaults
print("Custom values:", deploy_app("myapp", environment="production", replicas=3))

# TODO: Mutable default arguments (AVOID THIS!)
def bad_function(items=[]):  # DON'T DO THIS!
    """Bad: mutable default argument"""
    items.append("new")
    return items

# Better approach
def good_function(items=None):
    """Good: use None and create new list"""
    if items is None:
        items = []
    items.append("new")
    return items

print("\nBad function (shares state):", bad_function())
print("Bad function again:", bad_function())

print("\nGood function:", good_function())
print("Good function again:", good_function())

print()

# ========================================
# Exercise 3: *args and **kwargs
# ========================================
print("=" * 50)
print("Exercise 3: Variable Arguments")
print("=" * 50)

# TODO: *args - variable positional arguments
def check_servers(*server_names):
    """Check multiple servers"""
    print(f"Checking {len(server_names)} servers:")
    for server in server_names:
        print(f"  - {server}: OK")

check_servers("web-1", "web-2", "db-1")

# TODO: **kwargs - variable keyword arguments
def configure_server(server_name, **settings):
    """Configure server with variable settings"""
    print(f"\nConfiguring {server_name}:")
    for key, value in settings.items():
        print(f"  {key} = {value}")

configure_server("web-1", port=8080, memory="16GB", cpu_cores=4)

# TODO: Combining regular args, *args, and **kwargs
def deploy_to_servers(environment, *servers, **options):
    """Deploy to multiple servers with options"""
    print(f"\nDeploying to {environment}:")
    print(f"  Servers: {', '.join(servers)}")
    print(f"  Options: {options}")

deploy_to_servers(
    "production",
    "web-1", "web-2", "db-1",
    timeout=300,
    rollback=True,
    notify=True
)

print()

# ========================================
# Exercise 4: Type Hints
# ========================================
print("=" * 50)
print("Exercise 4: Type Hints")
print("=" * 50)

def calculate_uptime(start_time: float, end_time: float) -> float:
    """
    Calculate uptime in hours

    Args:
        start_time: Start timestamp
        end_time: End timestamp

    Returns:
        Uptime in hours
    """
    uptime_seconds = end_time - start_time
    uptime_hours = uptime_seconds / 3600
    return uptime_hours

uptime = calculate_uptime(1000.0, 5000.0)
print(f"Uptime: {uptime:.2f} hours")

# TODO: Type hints with collections
def filter_servers_by_status(
    servers: List[Dict[str, str]],
    status: str
) -> List[str]:
    """
    Filter servers by status

    Args:
        servers: List of server dictionaries
        status: Status to filter by

    Returns:
        List of server names matching status
    """
    return [
        server["name"]
        for server in servers
        if server.get("status") == status
    ]

servers = [
    {"name": "web-1", "status": "running"},
    {"name": "web-2", "status": "stopped"},
    {"name": "web-3", "status": "running"},
]

running_servers = filter_servers_by_status(servers, "running")
print(f"\nRunning servers: {running_servers}")

# TODO: Optional type hints
def get_config_value(
    key: str,
    default: Optional[str] = None
) -> Optional[str]:
    """
    Get configuration value with optional default

    Args:
        key: Configuration key
        default: Default value if key not found

    Returns:
        Configuration value or default
    """
    config = {"host": "localhost", "port": "8080"}
    return config.get(key, default)

print(f"\nHost: {get_config_value('host')}")
print(f"Timeout: {get_config_value('timeout', '30')}")

print()

# ========================================
# Exercise 5: Docstrings
# ========================================
print("=" * 50)
print("Exercise 5: Documentation with Docstrings")
print("=" * 50)

def backup_database(
    database_name: str,
    backup_dir: str,
    compress: bool = True
) -> Dict[str, Union[str, bool]]:
    """
    Backup a database to specified directory

    This function creates a backup of the specified database
    and optionally compresses it.

    Args:
        database_name: Name of the database to backup
        backup_dir: Directory to store backup
        compress: Whether to compress the backup (default: True)

    Returns:
        Dictionary containing:
            - success (bool): Whether backup succeeded
            - backup_file (str): Path to backup file
            - size (int): Size of backup in bytes

    Raises:
        ValueError: If database_name is empty
        IOError: If backup_dir is not writable

    Example:
        >>> result = backup_database("mydb", "/backups")
        >>> print(result["backup_file"])
        /backups/mydb_20240115.sql.gz
    """
    if not database_name:
        raise ValueError("database_name cannot be empty")

    # Simulate backup
    backup_file = f"{backup_dir}/{database_name}_backup.sql"
    if compress:
        backup_file += ".gz"

    return {
        "success": True,
        "backup_file": backup_file,
        "size": 1024000
    }

# Access docstring
print("Function docstring:")
print(backup_database.__doc__[:200] + "...")

# Use the function
result = backup_database("mydb", "/backups")
print(f"\nBackup result: {result}")

print()

# ========================================
# Exercise 6: Lambda Functions
# ========================================
print("=" * 50)
print("Exercise 6: Lambda Functions")
print("=" * 50)

# TODO: Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# TODO: Lambda with multiple arguments
add = lambda x, y: x + y
print(f"3 + 4 = {add(3, 4)}")

# TODO: Using lambda with built-in functions
servers = [
    {"name": "web-1", "cpu": 75},
    {"name": "web-2", "cpu": 45},
    {"name": "db-1", "cpu": 90},
]

# Sort by CPU usage
sorted_servers = sorted(servers, key=lambda s: s["cpu"], reverse=True)
print("\nServers sorted by CPU usage:")
for server in sorted_servers:
    print(f"  {server['name']}: {server['cpu']}%")

# TODO: Filter with lambda
high_cpu = list(filter(lambda s: s["cpu"] > 70, servers))
print(f"\nHigh CPU servers: {[s['name'] for s in high_cpu]}")

# TODO: Map with lambda
server_names = list(map(lambda s: s["name"], servers))
print(f"Server names: {server_names}")

print()

# ========================================
# Exercise 7: Function Composition
# ========================================
print("=" * 50)
print("Exercise 7: Function Composition")
print("=" * 50)

def validate_ip(ip: str) -> bool:
    """Validate IP address format"""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

def format_server_entry(name: str, ip: str) -> str:
    """Format server entry"""
    return f"{name:15} {ip}"

def create_server_config(servers: List[Dict[str, str]]) -> str:
    """Create server configuration from list"""
    lines = ["# Server Configuration", ""]

    for server in servers:
        name = server["name"]
        ip = server["ip"]

        if validate_ip(ip):
            line = format_server_entry(name, ip)
            lines.append(line)
        else:
            lines.append(f"# Invalid IP for {name}: {ip}")

    return "\n".join(lines)

# Use composed functions
servers = [
    {"name": "web-1", "ip": "192.168.1.10"},
    {"name": "web-2", "ip": "192.168.1.11"},
    {"name": "db-1", "ip": "invalid-ip"},
]

config = create_server_config(servers)
print("Generated configuration:")
print(config)

print()

# ========================================
# Exercise 8: Decorators
# ========================================
print("=" * 50)
print("Exercise 8: Decorators")
print("=" * 50)

# TODO: Simple decorator
def log_execution(func):
    """Decorator to log function execution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Completed {func.__name__}")
        return result
    return wrapper

@log_execution
def deploy_service(service_name):
    """Deploy a service"""
    print(f"  Deploying {service_name}")
    return f"{service_name} deployed"

result = deploy_service("web-app")
print(f"Result: {result}\n")

# TODO: Decorator with arguments
def retry(max_attempts=3):
    """Decorator to retry function on failure"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"  Attempt {attempt}/{max_attempts}")
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        print(f"  Failed after {max_attempts} attempts")
                        raise
                    print(f"  Error: {e}, retrying...")
            return None
        return wrapper
    return decorator

@retry(max_attempts=3)
def connect_to_server(server):
    """Simulate server connection with possible failure"""
    import random
    if random.random() < 0.6:  # 60% chance of failure
        raise ConnectionError(f"Failed to connect to {server}")
    return f"Connected to {server}"

print("Attempting connection with retry:")
try:
    result = connect_to_server("web-1")
    print(f"Success: {result}")
except ConnectionError:
    print("Failed to connect")

print()

# TODO: Timing decorator
def measure_time(func):
    """Measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@measure_time
def process_logs(num_lines):
    """Simulate log processing"""
    time.sleep(0.1)  # Simulate work
    return f"Processed {num_lines} lines"

print("Measuring execution time:")
result = process_logs(1000)
print(f"Result: {result}")

print()

# ========================================
# Exercise 9: Higher-Order Functions
# ========================================
print("=" * 50)
print("Exercise 9: Higher-Order Functions")
print("=" * 50)

def create_health_checker(threshold: int):
    """
    Create a health check function with specific threshold

    Args:
        threshold: CPU threshold percentage

    Returns:
        Function that checks if CPU is healthy
    """
    def check_health(cpu_usage: int) -> bool:
        """Check if CPU usage is below threshold"""
        return cpu_usage < threshold

    return check_health

# Create different checkers
strict_checker = create_health_checker(70)
lenient_checker = create_health_checker(90)

cpu_value = 80
print(f"CPU at {cpu_value}%:")
print(f"  Strict check (< 70%): {strict_checker(cpu_value)}")
print(f"  Lenient check (< 90%): {lenient_checker(cpu_value)}")

# TODO: Function that returns function
def create_formatter(prefix: str):
    """Create a formatter function with specific prefix"""
    def format_message(message: str) -> str:
        return f"{prefix}: {message}"
    return format_message

info = create_formatter("INFO")
error = create_formatter("ERROR")

print(f"\n{info('Service started')}")
print(f"{error('Connection failed')}")

print()

# ========================================
# Exercise 10: Best Practices
# ========================================
print("=" * 50)
print("Exercise 10: Best Practices")
print("=" * 50)

# 1. Single Responsibility
def read_server_list(filename: str) -> List[str]:
    """Read server list from file (one responsibility)"""
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def validate_servers(servers: List[str]) -> List[str]:
    """Validate server names (one responsibility)"""
    return [s for s in servers if s and not s.startswith('#')]

# 2. Pure functions (no side effects)
def calculate_total_memory(servers: List[Dict]) -> int:
    """Calculate total memory (pure function)"""
    return sum(server.get("memory", 0) for server in servers)

# 3. Descriptive names
def is_deployment_allowed(environment: str, time_of_day: int) -> bool:
    """Check if deployment is allowed (clear name)"""
    if environment == "production":
        return 9 <= time_of_day <= 17  # Business hours only
    return True

# 4. Keep functions small
def deploy_application(app_name: str, environment: str) -> bool:
    """Deploy application (delegates to smaller functions)"""
    if not validate_environment(environment):
        return False
    if not prepare_deployment(app_name):
        return False
    if not execute_deployment(app_name, environment):
        return False
    return verify_deployment(app_name)

def validate_environment(env: str) -> bool:
    """Validate environment"""
    return env in ["dev", "staging", "production"]

def prepare_deployment(app: str) -> bool:
    """Prepare deployment"""
    print(f"  Preparing {app}")
    return True

def execute_deployment(app: str, env: str) -> bool:
    """Execute deployment"""
    print(f"  Deploying {app} to {env}")
    return True

def verify_deployment(app: str) -> bool:
    """Verify deployment"""
    print(f"  Verifying {app}")
    return True

# Example usage
print("Deploying application:")
success = deploy_application("myapp", "production")
print(f"Deployment {'succeeded' if success else 'failed'}")

print("\n" + "=" * 50)
print("Lab 8 Complete!")
print("=" * 50)

# ========================================
# Your Tasks:
# ========================================
"""
1. Write a function that takes variable number of server names and returns their status

2. Create a function with type hints that:
   - Takes a list of dictionaries
   - Filters by a key-value pair
   - Returns filtered list

3. Write a decorator that logs:
   - Function name
   - Arguments passed
   - Return value
   - Execution time

4. Create a function that returns a function (closure) that remembers state

5. Write a higher-order function that takes a function and a list,
   applies the function to each item, and returns results

6. Create a retry decorator with:
   - Configurable max attempts
   - Configurable delay between retries
   - Exponential backoff

7. Write a function that validates server configuration:
   - Required fields present
   - Port number in valid range
   - IP address format correct
   - Use multiple smaller validation functions

8. Create a caching decorator that:
   - Stores function results
   - Returns cached result for same arguments
   - Has configurable cache size

9. Write a function composition utility:
   - Takes multiple functions
   - Returns a new function
   - Applies functions in sequence

10. Create a comprehensive server management module with:
    - Clear function names
    - Type hints
    - Docstrings
    - Single responsibility per function
    - Error handling
    - Proper return values
"""