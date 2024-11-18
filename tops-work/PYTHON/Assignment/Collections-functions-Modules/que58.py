"""
Que58. Write a Python program to read a random line from a file.
"""

import random

def read_random_line(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        
        # If the file is empty, return None
        if not lines:
            return None
        
        # Return a random line from the list
        return random.choice(lines).strip()  # strip() removes the trailing newline character

# Example usage
random_line = read_random_line('example.txt')
print(random_line)


