"""
Lab 7: Error Handling and Exception Management
===============================================
Objective: Handle errors gracefully and write robust DevOps scripts

Topics Covered:
- try/except blocks
- Catching specific exceptions
- Multiple exception handlers
- finally clause
- Raising exceptions
- Custom exceptions
- Context managers
- Best practices for error handling
"""

import os
import sys
import json
from datetime import datetime

# ========================================
# Exercise 1: Basic Exception Handling
# ========================================
print("=" * 50)
print("Exercise 1: Basic try/except")
print("=" * 50)

# TODO: Handle division by zero
print("Example 1: Division by zero")
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# TODO: Handle invalid type conversion
print("\nExample 2: Type conversion")
user_input = "not_a_number"
try:
    number = int(user_input)
    print(f"Number: {number}")
except ValueError:
    print(f"Error: '{user_input}' is not a valid number")

# TODO: Handle list index error
print("\nExample 3: List index")
servers = ["web-1", "web-2", "db-1"]
try:
    print(f"Server at index 5: {servers[5]}")
except IndexError:
    print("Error: Server index out of range")

print()

# ========================================
# Exercise 2: Catching Multiple Exceptions
# ========================================
print("=" * 50)
print("Exercise 2: Multiple Exception Types")
print("=" * 50)

def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid types for division")
        return None

# Test cases
print("Testing safe_divide:")
print(f"  10 / 2 = {safe_divide(10, 2)}")
print(f"  10 / 0 = {safe_divide(10, 0)}")
print(f"  10 / 'text' = {safe_divide(10, 'text')}")

# TODO: Catch multiple exceptions in one handler
print("\nCatching multiple exceptions:")
test_values = [10, "text", None]

for value in test_values:
    try:
        result = int(value) * 2
        print(f"  {value} * 2 = {result}")
    except (ValueError, TypeError) as e:
        print(f"  Error with {value}: {type(e).__name__}")

print()

# ========================================
# Exercise 3: Exception Information
# ========================================
print("=" * 50)
print("Exercise 3: Getting Exception Details")
print("=" * 50)

# TODO: Access exception details
print("Accessing exception information:")
try:
    data = {"server": "web-1"}
    print(data["missing_key"])
except KeyError as e:
    print(f"  Exception type: {type(e).__name__}")
    print(f"  Exception message: {e}")
    print(f"  Missing key: {e.args[0]}")

# TODO: Print full exception info
print("\nFull exception details:")
try:
    result = 10 / 0
except Exception as e:
    print(f"  Error: {e}")
    print(f"  Type: {type(e)}")
    import traceback
    print("  Traceback:")
    traceback.print_exc()

print()

# ========================================
# Exercise 4: finally Clause
# ========================================
print("=" * 50)
print("Exercise 4: Using finally")
print("=" * 50)

def read_config_file(filename):
    """Read configuration file with proper cleanup"""
    print(f"Attempting to read: {filename}")
    file_handle = None

    try:
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print(f"Successfully read {len(content)} characters")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'")
        return None
    finally:
        print("Cleanup: Closing file handle")
        if file_handle:
            file_handle.close()

# Test with non-existent file
print("Test 1: Non-existent file")
read_config_file("nonexistent.conf")

print("\nTest 2: Create and read file")
# Create a test file
test_file = "test_config.conf"
with open(test_file, 'w') as f:
    f.write("server=web-1\nport=8080\n")

read_config_file(test_file)

# Cleanup
os.remove(test_file)

print()

# ========================================
# Exercise 5: Raising Exceptions
# ========================================
print("=" * 50)
print("Exercise 5: Raising Exceptions")
print("=" * 50)

def validate_port(port):
    """Validate port number"""
    if not isinstance(port, int):
        raise TypeError("Port must be an integer")

    if port < 1 or port > 65535:
        raise ValueError(f"Port {port} is out of valid range (1-65535)")

    return True

# TODO: Test validation
print("Testing port validation:")
test_ports = [8080, -1, 70000, "8080"]

for port in test_ports:
    try:
        if validate_port(port):
            print(f"  Port {port}: Valid")
    except (TypeError, ValueError) as e:
        print(f"  Port {port}: Invalid - {e}")

print()

# ========================================
# Exercise 6: Custom Exceptions
# ========================================
print("=" * 50)
print("Exercise 6: Custom Exception Classes")
print("=" * 50)

# TODO: Define custom exceptions
class ServerError(Exception):
    """Base exception for server-related errors"""
    pass

class ServerNotFoundError(ServerError):
    """Raised when server is not found"""
    def __init__(self, server_name):
        self.server_name = server_name
        super().__init__(f"Server '{server_name}' not found")

class ServerNotResponding(ServerError):
    """Raised when server is not responding"""
    def __init__(self, server_name, timeout):
        self.server_name = server_name
        self.timeout = timeout
        super().__init__(f"Server '{server_name}' not responding after {timeout}s")

class DeploymentError(Exception):
    """Raised when deployment fails"""
    def __init__(self, message, server, step):
        self.server = server
        self.step = step
        super().__init__(f"Deployment failed on {server} at step '{step}': {message}")

# TODO: Use custom exceptions
def check_server(server_name):
    """Simulate server check"""
    known_servers = ["web-1", "web-2", "db-1"]

    if server_name not in known_servers:
        raise ServerNotFoundError(server_name)

    # Simulate timeout on web-2
    if server_name == "web-2":
        raise ServerNotResponding(server_name, timeout=30)

    return True

# Test custom exceptions
print("Testing custom exceptions:")
servers_to_check = ["web-1", "web-2", "web-3"]

for server in servers_to_check:
    try:
        check_server(server)
        print(f"  {server}: OK")
    except ServerNotFoundError as e:
        print(f"  {server}: ERROR - {e}")
    except ServerNotResponding as e:
        print(f"  {server}: TIMEOUT - {e}")
    except ServerError as e:
        print(f"  {server}: ERROR - {e}")

print()

# ========================================
# Exercise 7: else Clause
# ========================================
print("=" * 50)
print("Exercise 7: try/except/else/finally")
print("=" * 50)

def process_config(config_data):
    """Process configuration data"""
    try:
        # Try to parse JSON
        config = json.loads(config_data)
    except json.JSONDecodeError as e:
        print(f"  Error parsing JSON: {e}")
        return None
    else:
        # This runs only if no exception occurred
        print(f"  Successfully parsed config with {len(config)} items")
        return config
    finally:
        # This always runs
        print(f"  Finished processing")

# Test with valid and invalid JSON
print("Test 1: Valid JSON")
valid_json = '{"server": "web-1", "port": 8080}'
process_config(valid_json)

print("\nTest 2: Invalid JSON")
invalid_json = '{"server": "web-1", "port": }'
process_config(invalid_json)

print()

# ========================================
# Exercise 8: Context Managers
# ========================================
print("=" * 50)
print("Exercise 8: Context Managers (with statement)")
print("=" * 50)

# TODO: File handling with context manager
print("Writing and reading file with context manager:")

filename = "test_context.txt"

# Write file
try:
    with open(filename, 'w') as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.write("Line 3\n")
    print(f"  Successfully wrote to {filename}")
except IOError as e:
    print(f"  Error writing file: {e}")

# Read file
try:
    with open(filename, 'r') as f:
        content = f.read()
        print(f"  Read {len(content)} characters")
except IOError as e:
    print(f"  Error reading file: {e}")

# File is automatically closed
print(f"  File closed: {f.closed}")

# Cleanup
os.remove(filename)

print()

# ========================================
# Exercise 9: Real DevOps Scenario - Deployment Script
# ========================================
print("=" * 50)
print("Exercise 9: Robust Deployment Script")
print("=" * 50)

class DeploymentManager:
    """Manage deployment with proper error handling"""

    def __init__(self, servers):
        self.servers = servers
        self.results = []

    def deploy_to_server(self, server):
        """Deploy to a single server"""
        steps = ["backup", "stop_service", "deploy", "start_service", "verify"]

        try:
            print(f"\n  Deploying to {server}:")

            for step in steps:
                print(f"    - {step}...", end=" ")

                # Simulate failure on web-2 during deploy
                if server == "web-2" and step == "deploy":
                    raise DeploymentError("Package corrupted", server, step)

                # Simulate success
                print("OK")

            return {"server": server, "status": "success", "error": None}

        except DeploymentError as e:
            print(f"FAILED")
            print(f"    Error: {e}")
            return {"server": server, "status": "failed", "error": str(e)}

        except Exception as e:
            print(f"FAILED")
            print(f"    Unexpected error: {e}")
            return {"server": server, "status": "failed", "error": str(e)}

    def deploy_all(self):
        """Deploy to all servers"""
        print("Starting deployment:")

        for server in self.servers:
            result = self.deploy_to_server(server)
            self.results.append(result)

        # Summary
        print("\n" + "=" * 50)
        print("Deployment Summary:")
        success_count = sum(1 for r in self.results if r["status"] == "success")
        failed_count = len(self.results) - success_count

        print(f"  Total servers: {len(self.results)}")
        print(f"  Successful: {success_count}")
        print(f"  Failed: {failed_count}")

        if failed_count > 0:
            print("\n  Failed servers:")
            for result in self.results:
                if result["status"] == "failed":
                    print(f"    - {result['server']}: {result['error']}")

# Run deployment
servers = ["web-1", "web-2", "db-1"]
deployment = DeploymentManager(servers)
deployment.deploy_all()

print()

# ========================================
# Exercise 10: Error Handling Best Practices
# ========================================
print("=" * 50)
print("Exercise 10: Best Practices Summary")
print("=" * 50)

def best_practices_example():
    """Demonstrate error handling best practices"""

    # 1. Be specific with exceptions
    print("1. Catch specific exceptions:")
    try:
        data = json.loads('invalid json')
    except json.JSONDecodeError:  # Specific
        print("   JSON parse error")
    except Exception:  # Generic fallback
        print("   Other error")

    # 2. Don't catch exceptions you can't handle
    print("\n2. Don't silence errors you can't handle")

    # 3. Use finally for cleanup
    print("\n3. Use finally for cleanup:")
    resource = None
    try:
        resource = "acquired"
        print(f"   Resource: {resource}")
    finally:
        if resource:
            print(f"   Cleanup: releasing {resource}")

    # 4. Provide useful error messages
    print("\n4. Provide context in error messages")
    server = "web-1"
    try:
        # Some operation
        raise ConnectionError(f"Failed to connect to {server} on port 8080 after 3 retries")
    except ConnectionError as e:
        print(f"   Error: {e}")

    # 5. Log errors
    print("\n5. Log errors for debugging:")
    try:
        result = 10 / 0
    except Exception as e:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "error_type": type(e).__name__,
            "error_message": str(e),
            "severity": "ERROR"
        }
        print(f"   Log: {json.dumps(log_entry, indent=2)}")

best_practices_example()

print("\n" + "=" * 50)
print("Lab 7 Complete!")
print("=" * 50)

# ========================================
# Your Tasks:
# ========================================
"""
1. Write a function that reads a file and handles:
   - FileNotFoundError
   - PermissionError
   - IOError
   With appropriate error messages

2. Create a custom exception class for API errors that includes:
   - Status code
   - Error message
   - Timestamp

3. Write a function that validates user input with try/except:
   - Check if value is a number
   - Check if it's in valid range
   - Raise appropriate exceptions

4. Create a context manager for database connections that:
   - Opens connection in __enter__
   - Closes connection in __exit__
   - Handles exceptions properly

5. Write a deployment function that:
   - Tries multiple deployment methods
   - Falls back to alternative methods on failure
   - Logs all attempts
   - Raises exception only if all methods fail

6. Create a retry decorator that:
   - Retries a function N times on failure
   - Waits between retries
   - Logs each attempt
   - Re-raises exception after max retries

7. Write a configuration loader that:
   - Tries to load from multiple locations
   - Validates configuration
   - Provides defaults for missing values
   - Handles malformed config files

8. Create a health check system that:
   - Checks multiple services
   - Handles timeout errors
   - Handles connection errors
   - Reports partial failures
   - Never crashes completely

9. Build an error recovery system that:
   - Catches errors during processing
   - Logs errors
   - Continues processing remaining items
   - Reports summary at the end

10. Write a robust API client that handles:
    - Network errors
    - Timeout errors
    - HTTP errors (4xx, 5xx)
    - JSON decode errors
    - Retries with exponential backoff
"""