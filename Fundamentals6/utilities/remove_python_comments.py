import sys

def remove_comment_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if not line.strip().startswith('#'):
                file.write(line)

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
else:
    remove_comment_lines(sys.argv[1])
