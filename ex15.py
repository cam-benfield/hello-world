# Imports argv from sys
from sys import argv
# assigns variable names to the script and to the second argument
script, filename = argv
# opens the file in order to read it, otherwise, it's just a string
txt = open(filename)
# reads the file line by line
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
