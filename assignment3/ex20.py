from sys import argv # imports the argv function from sys

script, input_file = argv # defines the argv variables

def print_all(f):
    print(f.read()) # defines print_all as reading the file

def rewind(f):
    f.seek(0) # goes back to line 0

def print_a_line(line_count, f):
    print(line_count, f.readline()) # Defines print_a_line as reading whichever line is specified

current_file = open(input_file) # defines current_file

print("First let's print the whole file:\n") # prints what's in the ""

print_all(current_file) # prints current_file

print("Now let's rewind, kind of like a tape.") # prints what's in the ""

rewind(current_file) # goes back to line 0 of current_file

print("Let's print three lines:") # prints what's in the ""

current_line = 1
print_a_line(current_line, current_file) # prints what's on line 1

current_line = current_line + 1 # prints what's on line 1+1
print_a_line(current_line, current_file)

current_line = current_line + 1 # prints what's on line 2+1
print_a_line(current_line, current_file)
