#!/bin/bash

# check_permissions.sh
# Usage: ./check_permissions.sh <file_or_dir_path> <expected_permissions>
# Example: ./check_permissions.sh /etc/passwd 644

# --- MAIN SCRIPT ---

# 1. Argument check
if [ $# -ne 2 ]; then
    echo "Please provide both file name and it's permissions"
	exit 1	
fi

FILE_NAME="$1"
EXPECTED_PERM="$2"

# 2. Check if file/directory exists
if [ ! -e "$FILE_NAME" ]; then
    error "File or directory '$FILE_NAME' does not exist." 
	exit 2
fi

# 3. Get current permissions (octal)
ACTUAL_PERM=$(stat -c "%a" "$FILE_NAME")
if [ "$ACTUAL_PERM" != "$EXPECTED_PERM" ]; then
    echo "Permission MISMATCH: $FILE_NAME has $ACTUAL_PERM, expected $EXPECTED_PERM"
    exit 3
else
    echo "Permission OK: $FILE_NAME has expected permission $EXPECTED_PERM"
fi

# 4. Ownership check
OWNER=$(stat -c "%U" "$FILE_NAME")
CURRENT_USER=$(whoami)
if [ "$OWNER" != "$CURRENT_USER" ]; then
    echo "Ownership WARNING: $FILE_NAME is owned by $OWNER, not $CURRENT_USER"
    exit 4
else
    echo "Ownership OK: $FILE_NAME is owned by $CURRENT_USER"
fi

# 5. Security check: world-writable
PERM_STR=$(stat -c "%A" "$FILE_NAME")
if [[ $PERM_STR =~ .w..w..w. ]]; then
    echo "SECURITY ISSUE: $FILE_NAME is world-writable!"
    exit 5
fi

# 6. Security check: group-writable
if [[ $PERM_STR =~ ..w.... ]]; then
    echo "SECURITY NOTICE: $FILE_NAME is group-writable."
	exit 5
fi

# Exit codes:
# 0 - OK
# 1 - Arguments not complete
# 2 - File does not exist
# 3 - Permission mismatch
# 4 - Ownership issue
# 5 - World-writable security issue