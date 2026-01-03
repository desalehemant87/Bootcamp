import subprocess
output = subprocess.run(["ls", "-l"])
print("Return code:", output.returncode)
print("STDOUT:", output.stdout) 
print("STDERR:", output.stderr)
print("-----------------------------")

# Note: To capture output, use subprocess.run with capture_output=True
output = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("Output:", output)
print("Return code:", output.returncode)
print("STDOUT:\n", output.stdout)
print("STDERR:\n", output.stderr)

out = output.stdout
lines = out.splitlines()
print("Number of lines in output:", len(lines)) 
print("First 5 lines of output:")
for line in lines[1:5]:
    # print filename only
    parts = line.split()    
    if len(parts) >= 9:
        print(parts[8])
    else:
        print(line)
print("-----------------------------")  





