from sys import argv

script, filename = argv

hi = open(filename)
print(f"Here's your file {filename}.")
print(hi.read())
