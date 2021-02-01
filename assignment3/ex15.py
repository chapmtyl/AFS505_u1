from sys import argv # This imports the argv function from sys

script, filename = argv # this defines what you type as filename

txt = open(filename) #defines txt as opening the filename

print(f"Here's your file {filename}:") # Prints here's your file "filename"
print(txt.read()) # reads the txt variable

print("Type the filename again:") #prints "type the filename again"
file_again = input("> ") # Defines file_again as whatever you type in

txt_again = open(file_again) #defines txt_again as opening whatever you typed in

print(txt_again.read()) # prints the contents of the file you typed in.
