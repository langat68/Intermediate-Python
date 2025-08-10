file = open("example.txt", "r")  # 'r' means read mode
"r" # Read (default). Fails if the file doesn’t exist.

"w" # Write. Creates a new file or overwrites existing content.

"a" # Append. Creates the file if it doesn’t exist and writes at the end.

"x" #  Create. Fails if the file exists.



# 1. Reading files
file = open("example.txt", "r")

# Read entire file
content = file.read()
print(content)

# OR read line-by-line
file.seek(0)  # Reset cursor to start
for line in file:
    print(line.strip())  # strip() removes \n

file.close()


# 2 Writing to a File

file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This will overwrite existing content.\n")
file.close()



# 3 Appending to a File

file = open("example.txt", "a")
file.write("Adding this line at the end.\n")
file.close()
