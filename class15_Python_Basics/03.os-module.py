import os
print("Current working directory:", os.getcwd())
# . is used to indicate current directory
print("List of files and directories in current directory:", os.listdir('.'))   
# r is used to indicate raw string so that backslashes are treated literally 
print("List of files and directories in current directory:", os.listdir(r"D:\DevOps_Bootcamp\Bootcamp\class15_Python_Basics"))   
# double back slashes to escape backslash character
print("List of files and directories in current directory:", os.listdir("D:\\DevOps_Bootcamp\\Bootcamp\\class15_Python_Basics"))
# forward slashes also work on Windows
print("List of files and directories in current directory:", os.listdir(r"D:/DevOps_Bootcamp/Bootcamp/class15_Python_Basics"))
print("Creating a new directory 'test_dir'")
os.mkdir('test_dir')
print("List of files and directories after creating 'test_dir':", os.listdir('.'))
print("Changing current working directory to 'test_dir'")   
os.chdir('test_dir')
print("Current working directory after change:", os.getcwd())
print("Changing back to parent directory")   
os.chdir('..')
print("Current working directory after changing back:", os.getcwd())
print("Removing the directory 'test_dir'")   
os.rmdir('test_dir')
print("List of files and directories after removing 'test_dir':", os.listdir('.'))

# print all the attributes and methods of os module
#print(dir(os))
#print(help(os))

status = os.system('touch testfile.txt')  # works on Unix/Linux/Mac
print("Status of touch command:", status)

# WEXITSTATUS is not available on Windows, it works on Unix/Linux/Mac
#print("status code", os.WEXITSTATUS(status))

print("os name:", os.name)
os.system('ls -l')            # works on Unix/Linux/Mac
os.system('rm testfile.txt')   # works on Unix/Linux/Mac
os.system('ls -l')            # works on Unix/Linux/Mac

# On Windows, you can use the following commands instead:
# os.system('type nul > testfile.txt')  # create an empty file
# os.system('dir')                     # list files and directories
# os.system('del testfile.txt')        # delete the file


def count_dir_file(path='.', include_root=False, min_size_kb=10):
    """Walk the given path and return (dir_count, file_count).
    Also prints files larger than min_size_kb and their count."""
    if not os.path.exists(path):
        print("Path does not exist:", path)
        return 0, 0
    if not os.path.isdir(path):
        print("Provided path is not a directory:", path)
        return 0, 0

    dir_count = 0
    file_count = 0
    large_files = []
    threshold = min_size_kb * 1024

    for root, dirs, files in os.walk(path):
        dir_count += len(dirs)
        file_count += len(files)
        print("Current directory:", root)
        print("Sub-directories:", dirs)
        print("Files:", files)
        for fname in files:
            full_path = os.path.join(root, fname)
            try:
                size = os.path.getsize(full_path)
            except OSError as e:
                print("Could not get size for", full_path, ":", e)
                continue
            if size > threshold:
                large_files.append((full_path, size))

    if include_root:
        dir_count += 1

    if large_files:
        print(f"Files larger than {min_size_kb} KB:")
        for p, s in large_files:
            print(f"{p} - {s/1024:.2f} KB")
    else:
        print(f"No files larger than {min_size_kb} KB found.")
    print("Large files count:", len(large_files))

    return dir_count, file_count

# call the function and print the results
path = input("Enter path to walk (default: current directory): ").strip() or '.'
dir_count, file_count = count_dir_file(path)
print("Total directories:", dir_count)
print("Total files:", file_count)

# os.system() to run shell commands, but it may not capture output directly.
print("Running 'ps aux' command to list processes:")
output = os.system('ps aux')  # works on Unix/Linux/Mac
print("Output of 'ps aux' command:", output)
print("type of output:", type(output)) # this is wrong way to capture output. type is wrong.
print("-----------------------------")

# print("Environment Variables:")
# for key, value in os.environ.items():
#     print(f"{key}: {value}")
print("-----------------------------")
home_dir = os.environ.get('HOME') or os.environ.get('USERPROFILE')
print("Home Directory from environment variable:", home_dir)
print("-----------------------------")
print("Joining paths:")
path1 = os.path.join(home_dir, 'documents', 'file.txt')
print("Joined path:", path1)
print("Splitting paths:")
dir_name, file_name = os.path.split(path1)
print("Directory name:", dir_name)
print("File name:", file_name)
base_name, ext = os.path.splitext(file_name)
print("Base name:", base_name)
print("Extension:", ext)
print("-----------------------------")
print("Checking path existence and type:")
print(f"Does path '{path1}' exist?", os.path.exists(path1))
print(f"Is path '{path1}' a file?", os.path.isfile(path1))
print(f"Is path '{path1}' a directory?", os.path.isdir(path1))
print("-----------------------------")