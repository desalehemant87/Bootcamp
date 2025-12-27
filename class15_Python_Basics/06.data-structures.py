"""
Lab 1: Python Data Structures for DevOps
==========================================
Objective: Master lists, dictionaries, tuples, and sets with real DevOps scenarios

Topics Covered:
- Lists: Managing server lists, logs, commands
- Dictionaries: Configuration management, server metadata
- Tuples: Immutable data like coordinates, constants
- Sets: Unique items, comparing environments
"""

# ========================================
# Exercise 1: Lists - Managing Servers
# ========================================
print("=" * 50)
print("Exercise 1: Working with Server Lists")
print("=" * 50)

# TODO: Create a list of server names
servers = ["web-server-1", "web-server-2", "db-server-1", "cache-server-1"]
print(f"All servers: {servers}")

# TODO: Add a new server to the list
servers.append("web-server-3")
print(f"After adding new server: {servers}")

# TODO: Remove a server from the list
servers.remove("cache-server-1")
print(f"After removing cache server: {servers}")

# TODO: Check if a server exists
if "db-server-1" in servers:
    print("Database server is in the list")

# TODO: Get the first and last server
print(f"First server: {servers[0]}")
print(f"Last server: {servers[-1]}")

# TODO: Slice to get web servers (first 3)
web_servers = servers[:3]
print(f"Web servers: {web_servers}")

print()

# ========================================
# Exercise 2: Dictionaries - Server Configuration
# ========================================
print("=" * 50)
print("Exercise 2: Server Configuration with Dictionaries")
print("=" * 50)

# TODO: Create a dictionary for server configuration
server_config = {
    "hostname": "web-server-1",
    "ip_address": "192.168.1.10",
    "port": 8080,
    "status": "running",
    "cpu_cores": 4,
    "memory_gb": 16
}

print(f"Server config: {server_config}")

# TODO: Access specific values
print(f"Hostname: {server_config['hostname']}")
print(f"IP Address: {server_config['ip_address']}")

# TODO: Update a value
print(f"Initial status: {server_config['status']}")
server_config["status"] = "stopped"
print(f"Updated status: {server_config['status']}")

# TODO: Add a new key-value pair
server_config["os"] = "Ubuntu 22.04"
print(f"Added OS: {server_config['os']}")

# TODO: Use get() method with default value
backup_enabled = server_config.get("backup", False)
print(f"Backup enabled: {backup_enabled}")

# TODO: Iterate through dictionary
# dict.items() will output key-value pairs as tuples 
print("\nAll configuration items:")
print(server_config.items())
print("\nIterating through config:\n")
for key, value in server_config.items():
    print(f"{key}: {value}")

print()

# ========================================
# Exercise 3: Nested Dictionaries - Multiple Servers
# ========================================
print("=" * 50)
print("Exercise 3: Managing Multiple Servers")
print("=" * 50)

# TODO: Create nested dictionary for infrastructure
infrastructure = {
    "web-server-1": {
        "ip": "192.168.1.10",
        "status": "running",
        "services": ["nginx", "nodejs"]
    },
    "web-server-2": {
        "ip": "192.168.1.11",
        "status": "running",
        "services": ["nginx", "nodejs"]
    },
    "db-server-1": {
        "ip": "192.168.1.20",
        "status": "running",
        "services": ["postgresql", "redis"]
    }
}

# TODO: Access nested data
print(f"Web Server 1 IP: {infrastructure['web-server-1']['ip']}")
print(f"DB Server services: {infrastructure['db-server-1']['services']}")

# TODO: Add a new server
infrastructure["monitoring-server"] = {
    "ip": "192.168.1.30",
    "status": "running",
    "services": ["prometheus", "grafana"]
}

# TODO: Iterate through all servers
print("\nAll servers in infrastructure:\n")
print(infrastructure.items ())
print("\nIterating through infrastructure:\n")
for server_name, server_info in infrastructure.items():
    print(f"\n{server_name}:")
    print(f"  IP: {server_info['ip']}")
    print(f"  Status: {server_info['status']}")
    print(f"  Services: {', '.join(server_info['services'])}")

print()

# ========================================
# Exercise 4: Tuples - Immutable Configuration
# ========================================
print("=" * 50)
print("Exercise 4: Tuples for Immutable Data")
print("=" * 50)

# TODO: Create tuples for fixed data
server_location = ("ap-south-1", "availability-zone-a")
print(f"Server location: {server_location}")

# TODO: Unpack tuple
region, zone = server_location
print(f"Region: {region}, Zone: {zone}")

# TODO: Create tuple of allowed ports
allowed_ports = (80, 443, 8080, 22)
print(f"Allowed ports: {allowed_ports}")

# TODO: Check if port is allowed
port_to_check = 443
if port_to_check in allowed_ports:
    print(f"Port {port_to_check} is allowed")

# TODO: Multiple tuples in a list (coordinates)
data_centers = [
    ("ap-south-1", 40.7128, -74.0060),
    ("ap-south-2", 37.7749, -122.4194),
    ("ap-west-1", 51.5074, -0.1278)
]

print("\nData center locations:")
for dc_name, lat, lon in data_centers:
    print(f"  data center: {dc_name}, Latitude: {lat}, Longitude: {lon}")

print()

# ========================================
# Exercise 5: Sets - Unique Items and Comparisons
# ========================================
print("=" * 50)
print("Exercise 5: Sets for Unique Items")
print("=" * 50)

# TODO: Create sets of installed packages on different servers
server1_packages = {"nginx", "python3", "git", "docker", "postgresql"}
server2_packages = {"nginx", "python3", "git", "redis", "mongodb"}

print(f"Server 1 packages: {server1_packages}")
print(f"Server 2 packages: {server2_packages}")

# TODO: Find common packages (intersection)
common_packages = server1_packages & server2_packages
print(f"\nCommon packages: {common_packages}")

# TODO: Find packages only in server1 (difference)
only_server1 = server1_packages - server2_packages
print(f"Only in Server 1: {only_server1}")

# TODO: Find packages only in server2
only_server2 = server2_packages - server1_packages
print(f"Only in Server 2: {only_server2}")

# TODO: Find all unique packages (union)
all_packages = server1_packages | server2_packages
print(f"All unique packages: {all_packages}")

# TODO: Add package to set
server1_packages.add("nodejs")
print(f"\nServer 1 after adding nodejs: {server1_packages}")

# TODO: Remove duplicates from a list using set
log_levels = ["INFO", "ERROR", "INFO", "DEBUG", "ERROR", "INFO", "WARNING"]
unique_log_levels = set(log_levels)
print(f"\nLog levels with duplicates: {log_levels}")
print(f"Unique log levels: {unique_log_levels}")

print()

# ========================================
# Practice Exercise: Combine All Data Structures
# ========================================
print("=" * 50)
print("Practice: Real DevOps Scenario")
print("=" * 50)

# Scenario: You need to manage deployment information

deployments = [
    {
        "app_name": "web-app",
        "version": "1.2.3",
        "servers": ["web-server-1", "web-server-2"],
        "env_vars": {"PORT": 8080, "DB_HOST": "192.168.1.20"},
        "allowed_ips": {"192.168.1.0", "10.0.0.0"},
        "coordinates": ("us-east-1", 40.7128, -74.0060)
    },
    {
        "app_name": "api-service",
        "version": "2.0.1",
        "servers": ["web-server-2", "web-server-3"],
        "env_vars": {"PORT": 3000, "CACHE_HOST": "192.168.1.15"},
        "allowed_ips": {"192.168.1.0", "172.16.0.0"},
        "coordinates": ("us-west-1", 37.7749, -122.4194)
    }
]

print("Deployment Information:")
for deployment in deployments:
    print(f"\n{deployment['app_name']} v{deployment['version']}:")
    print(f"  Servers: {', '.join(deployment['servers'])}")
    print(f"  Environment Variables:")
    for key, value in deployment['env_vars'].items():
        print(f"    {key}={value}")
    print(f"  Allowed IPs: {deployment['allowed_ips']}")
    region, lat, lon = deployment['coordinates']
    print(f"  Location: {region} ({lat}, {lon})")

print("\n" + "=" * 50)
print("Lab 1 Complete!")
print("=" * 50)
