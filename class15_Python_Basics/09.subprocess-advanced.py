"""
Lab 4: Subprocess Module for Shell Command Execution
=====================================================
Objective: Execute shell commands from Python and handle their output

Topics Covered:
- Running shell commands with subprocess.run()
- Capturing command output (stdout, stderr)
- Handling exit codes
- Running commands with arguments
- Piping commands
- Working with shell=True and shell=False
- Timeout handling
"""

import subprocess
import sys
import os

# ========================================
# Exercise 1: Basic Command Execution
# ========================================
print("=" * 50)
print("Exercise 1: Basic Command Execution")
print("=" * 50)

# TODO: Run a simple command
print("Running 'echo' command:")
result = subprocess.run(["echo", "Hello from subprocess!"])
print(f"Return code: {result.returncode}")

# TODO: Run command and capture output
print("\nRunning 'python --version':")
result = subprocess.run(
    ["python3", "--version"],
    capture_output=True,
    text=True
)
print(f"Output: {result.stdout.strip()}")
print(f"Return code: {result.returncode}")

# TODO: Platform-specific command
if sys.platform == "win32":
    # Windows
    result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
    print("\nWindows directory listing:")
    print(result.stdout[:200])  # First 200 chars
else:
    # Unix-like (Linux, macOS)
    result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
    print("\nDirectory listing:")
    print(result.stdout[:500])  # First 500 chars

print()

# ========================================
# Exercise 2: Capturing Output
# ========================================
print("=" * 50)
print("Exercise 2: Capturing Command Output")
print("=" * 50)

# TODO: Capture stdout
print("Checking disk usage:")
if sys.platform != "win32":
    result = subprocess.run(
        ["df", "-h", "."],
        capture_output=True,
        text=True
    )
    print(result.stdout)
else:
    result = subprocess.run(
        ["dir"],
        shell=True,
        capture_output=True,
        text=True
    )
    print(result.stdout[:300])

# TODO: Separate stdout and stderr
print("\nTesting stderr capture:")
# Run a command that doesn't exist
result = subprocess.run(
    ["nonexistent_command"],
    capture_output=True,
    text=True
)
if result.returncode != 0:
    print(f"Command failed with exit code: {result.returncode}")
    print(f"Error output: {result.stderr.strip()}")

print()

# ========================================
# Exercise 3: Working with Exit Codes
# ========================================
print("=" * 50)
print("Exercise 3: Exit Codes and Error Handling")
print("=" * 50)

# TODO: Check exit code
commands = [
    ["python3", "--version"],
    ["git", "--version"],
    ["docker", "--version"]
]

print("Checking installed tools:")
for cmd in commands:
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            output = result.stdout.strip() or result.stderr.strip()
            print(f"  {cmd[0]}: {output}")
        else:
            print(f"  {cmd[0]}: Command failed (exit code {result.returncode})")
    except FileNotFoundError:
        print(f"  {cmd[0]}: Not installed")
    except subprocess.TimeoutExpired:
        print(f"  {cmd[0]}: Command timed out")

# TODO: Using check=True to raise exception on failure
print("\nUsing check=True:")
try:
    result = subprocess.run(
        ["python3", "--version"],
        check=True,
        capture_output=True,
        text=True
    )
    print(f"Success: {result.stdout.strip()}")
except subprocess.CalledProcessError as e:
    print(f"Command failed: {e}")

print()

# ========================================
# Exercise 4: Running Commands with Arguments
# ========================================
print("=" * 50)
print("Exercise 4: Commands with Arguments")
print("=" * 50)

# TODO: Create a test file first
test_file = "test_subprocess.txt"
with open(test_file, "w") as f:
    f.write("Line 1: Hello World\n")
    f.write("Line 2: Python for DevOps\n")
    f.write("Line 3: Subprocess module\n")
    f.write("Line 4: Shell commands\n")

print(f"Created test file: {test_file}")

# TODO: Use grep/findstr to search file
if sys.platform != "win32":
    # Unix-like systems
    print("\nSearching for 'Python' in file:")
    result = subprocess.run(
        ["grep", "Python", test_file],
        capture_output=True,
        text=True
    )
    print(result.stdout)

    print("Counting lines in file:")
    result = subprocess.run(
        ["wc", "-l", test_file],
        capture_output=True,
        text=True
    )
    print(result.stdout.strip())
else:
    # Windows
    print("\nSearching for 'Python' in file:")
    result = subprocess.run(
        ["findstr", "Python", test_file],
        capture_output=True,
        text=True
    )
    print(result.stdout)

print()

# ========================================
# Exercise 5: Using shell=True (Use with Caution!)
# ========================================
print("=" * 50)
print("Exercise 5: Shell=True vs Shell=False")
print("=" * 50)

# TODO: shell=False (safer, recommended)
print("Using shell=False (safe):")
result = subprocess.run(
    ["echo", "Hello, World!"],
    capture_output=True,
    text=True
)
print(f"Output: {result.stdout.strip()}")

# TODO: shell=True (allows shell features but less safe)
print("\nUsing shell=True (allows pipes, redirects):")
if sys.platform != "win32":
    result = subprocess.run(
        "echo 'Hello' | wc -c",
        shell=True,
        capture_output=True,
        text=True
    )
    print(f"Character count: {result.stdout.strip()}")
else:
    result = subprocess.run(
        "echo Hello",
        shell=True,
        capture_output=True,
        text=True
    )
    print(f"Output: {result.stdout.strip()}")

print()

# ========================================
# Exercise 6: Real DevOps Scenario - System Information
# ========================================
print("=" * 50)
print("Exercise 6: Gathering System Information")
print("=" * 50)

system_info = {}

# TODO: Get system information
if sys.platform != "win32":
    # Unix-like systems
    commands = {
        "hostname": ["hostname"],
        "os": ["uname", "-s"],
        "kernel": ["uname", "-r"],
        "uptime": ["uptime"],
    }
else:
    # Windows
    commands = {
        "hostname": ["hostname"],
        "os": ["ver"],
    }

print("System Information:")
for key, cmd in commands.items():
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            system_info[key] = output
            print(f"  {key.title()}: {output}")
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f"  {key.title()}: Unable to retrieve")

print()

# ========================================
# Exercise 7: Running Git Commands
# ========================================
print("=" * 50)
print("Exercise 7: Git Commands (if git is available)")
print("=" * 50)

# TODO: Check if we're in a git repository
try:
    result = subprocess.run(
        ["git", "rev-parse", "--git-dir"],
        capture_output=True,
        text=True,
        timeout=5
    )

    if result.returncode == 0:
        print("This is a Git repository")

        # Get git status
        print("\nGit Status:")
        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True
        )
        status = result.stdout.strip()
        if status:
            print(status)
        else:
            print("  Working directory clean")

        # Get current branch
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True
        )
        branch = result.stdout.strip()
        print(f"\nCurrent branch: {branch}")

        # Get last commit
        result = subprocess.run(
            ["git", "log", "-1", "--oneline"],
            capture_output=True,
            text=True
        )
        last_commit = result.stdout.strip()
        print(f"Last commit: {last_commit}")
    else:
        print("Not a Git repository")

except FileNotFoundError:
    print("Git is not installed")
except subprocess.TimeoutExpired:
    print("Git command timed out")

print()

# ========================================
# Exercise 8: Process Management
# ========================================
print("=" * 50)
print("Exercise 8: Process Information")
print("=" * 50)

if sys.platform != "win32":
    # Check running Python processes
    print("Python processes:")
    result = subprocess.run(
        ["ps", "aux"],
        capture_output=True,
        text=True
    )
    lines = result.stdout.split("\n")
    python_processes = [line for line in lines if "python" in line.lower()]

    if python_processes:
        print(f"Found {len(python_processes)} Python process(es)")
        for proc in python_processes[:3]:  # Show first 3
            print(f"  {proc}")
    else:
        print("No Python processes found")
else:
    # Windows
    print("Python processes:")
    result = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq python.exe"],
        capture_output=True,
        text=True
    )
    print(result.stdout[:300])

print()

# ========================================
# Exercise 9: Timeout Handling
# ========================================
print("=" * 50)
print("Exercise 9: Handling Command Timeouts")
print("=" * 50)

# TODO: Command with timeout
print("Running command with 2-second timeout:")
try:
    # This command should complete quickly
    result = subprocess.run(
        ["python3", "--version"],
        capture_output=True,
        text=True,
        timeout=2
    )
    print(f"Success: {result.stdout.strip()}")
except subprocess.TimeoutExpired:
    print("Command timed out!")

print()

# ========================================
# Exercise 10: Building a Simple Deployment Check
# ========================================
print("=" * 50)
print("Exercise 10: Pre-Deployment Checks")
print("=" * 50)

def run_check(name, command, success_message):
    """Run a deployment check command"""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"  {name}: PASS - {success_message}")
            return True
        else:
            print(f"  {name}: FAIL - Exit code {result.returncode}")
            return False
    except FileNotFoundError:
        print(f"  {name}: FAIL - Command not found")
        return False
    except subprocess.TimeoutExpired:
        print(f"  {name}: FAIL - Timeout")
        return False

# Run pre-deployment checks
print("Running pre-deployment checks:")
checks = [
    ("Python", ["python3", "--version"], "Python is installed"),
    ("Git", ["git", "--version"], "Git is installed"),
    ("Disk Space", ["df" if sys.platform != "win32" else "dir", "."], "Sufficient disk space"),
]

results = []
for name, cmd, success_msg in checks:
    results.append(run_check(name, cmd, success_msg))

# Summary
print(f"\nChecks passed: {sum(results)}/{len(results)}")
if all(results):
    print("All checks passed - Ready for deployment!")
else:
    print("Some checks failed - Please fix issues before deployment")

print("\n" + "=" * 50)
print("Lab 4 Complete!")
print("=" * 50)

# Cleanup
if os.path.exists(test_file):
    os.remove(test_file)
    print(f"\nCleaned up: {test_file}")

# ========================================
# Your Tasks:
# ========================================
"""
1. Write code to execute 'ls -la' (or 'dir' on Windows) and print the output

2. Create a function that runs a command and returns True if it succeeds, False otherwise

3. Write code to check if Docker is installed and print its version

4. Create a script that:
   - Creates a directory
   - Creates a file in that directory
   - Lists the contents using subprocess
   - Deletes the directory

5. Write a function that runs a command with a timeout and handles the timeout exception

6. Use subprocess to run 'git status' and parse the output to check if there are uncommitted changes

7. Create a health check script that:
   - Checks if required services are running
   - Checks disk space
   - Checks if required ports are available
   - Returns a summary report

8. Write code that runs multiple commands in sequence and stops if any command fails

9. Create a function that runs a shell command and logs both stdout and stderr to separate files

10. Build a simple backup script using subprocess that:
    - Creates a tar archive of a directory (Unix) or zip (Windows)
    - Verifies the archive was created successfully
    - Prints the size of the backup
"""