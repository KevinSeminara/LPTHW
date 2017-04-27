from sys import argv

script, input_file = argv

# function to print all lines of txt file
def print_all(f):
    print f.read()

# sets the file back to the first line for the read function
def rewind(f):
    f.seek(0)

# takes in a line number and prints out that number and the line from the text file
def print_a_line(line_count, f):
    print line_count, f.readline()

# set current_file to whatever text file was put as an argument
current_file = open(input_file)

print "First let's print the whole file:\n"

# print all lines from the inputted file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# set the read back to the first line of file
rewind(current_file)

print "Let's print three lines:"

# set the current line to 1
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

