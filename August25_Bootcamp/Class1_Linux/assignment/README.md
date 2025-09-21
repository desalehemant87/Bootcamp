File Permission Checker
This script is designed to automate the task of verifying file and directory permissions. It ensures that files are secure, meet the specified permission standards, and are owned by the correct user.

Features:
Verifies file permissions against expected values (e.g., 644, 755).
Flags world-writable files and alerts about potential security risks.
Ensures that files are owned by the correct user to maintain system integrity.
Usage:
Clone the repository.
Navigate to the August25_Bootcamp/Class1_Linux/assignment folder.
Run the script with the following command:
./check_permissions.sh <file/directory> <expected_permissions>