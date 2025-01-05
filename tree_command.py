"""
Problem - Implement tree command where input will have seprate path of directory
Domain:
    0 < path < 100 
Error
    
Edge Case
    No path -  print tree of current directory
Data
    number_of_path = number of path given in input
    

Algorithm   
"""
import os
import sys

PIPE = "│"
NESTED_FILE = "└──"
OUTER_FILE = "├──"
PIPE_WITH_SPACE = "│   "
SPACE = "    "

def print_tree(path, prefix=""):
    entries = os.listdir(path)
    # print(entries)
    for index, entry in enumerate(entries):
        new_path = os.path.join(path, entry)
        sequence = "└── " if index == len(entries) - 1 else "├── "
        print(f"{prefix}{sequence}{entry}")
        if os.path.isdir(new_path):
            new_prefix = "    " if index == len(entries) - 1 else "│   "
            print_tree(path, path+new_prefix)
             


def main():
    paths =  sys.argv[2:]
    print(paths)
    for path in paths:
        print("\n")
        print(f"Tree for: {path}")
        print(path)
        if os.path.exists(path):
            print_tree(path)
        else:
            print(f"Path {path} does not exist]")


if __name__ == "__main__":
        main()