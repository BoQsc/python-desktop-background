import sys

def remove_comments(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line.split('#')[0].rstrip() + '\n')

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
else:
    remove_comments(sys.argv[1])
