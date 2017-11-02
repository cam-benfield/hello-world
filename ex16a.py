from sys import argv

script, filename = argv

prompt = ">"

target = open(filename, 'w')
print "%s is open.\n" % filename

print "What would you like to do with %s?" % filename
print "If you would like to erase the file, type ERASE."
print "If you would like to append something to the file, type APPEND."
print "If you would like to close the file, type CLOSE."
print "If you would like to end this script, press CTRL-C."

action = raw_input(prompt).upper()
print "You would like to: %s" % action

if action == "CLOSE":
    target.close()
    print "File closed."
elif action == "ERASE":
    target.truncate()
    print "File erased."
elif action == "APPEND":
    print "Are you sure you want to APPEND stuff to this file?"
    print "That isn't set up. Please come back later."
else:
    print "Thanks for trying!"
    target.close()

target.close()
