from sys import argv
from os.path import exists

script, filename = argv

# Establishing Strings
prompt = ">"

# Establishing Functions
def startedit(userfilestr):
    print "What would you like to do with %s?" % userfilestr
    print "If you would like to erase the file, type ERASE."
    print "If you would like to copy this file into a new file, type COPY."
    print "If you would like to append something to the file, type APPEND."
    print "If you would like to close the file, type CLOSE."
    print "If you would like to suddenly end this script, press CTRL-C."
    editmode = raw_input(prompt).upper()
    return editmode


def addtofile(userfile):
    print "What would you like to write? [END will end appending]"
    datawrite = raw_input(prompt)
    if datawrite != "END":
        userfile.write(datawrite)
        userfile.write("\n")
        addtofile(userfile)
    elif datawrite == "END":
        pass
    return "Your information was added to %s!" % filename

def edittype(editmode, userfile):
    if editmode == "CLOSE":
        userfile.close()
        print "File closed."
    elif editmode == "ERASE":
        userfile.truncate()
        print "File erased."
    elif editmode == "APPEND":
        status = addtofile(userfile)
        print status
    elif editmode == "COPY":
        status = copyfile(userfile)
        print status
    else:
        print "Thanks for trying!"

def copyfile(userfile):
    print "What file would you like to copy?"
    print "Is it %s?" % userfile
    print "What would you like to name the new file?"
    newfilenameraw = raw_input(prompt)
    print "You would like to name it %s?" % newfilenameraw
    print "It will be named %s.txt" % newfilenameraw
    newfilename = "%s.txt" % newfilenameraw
    newfile = open(newfilename, 'w+')
    olddata = userfile.read()
    olddatalength = len(olddata)
    print "Total Data to be Copied: %d bytes." % olddatalength
    newfile.write(olddata)
    newfile.close()
    newfile = open(newfilename,'r')
    return "All Done."

# Actual script running
target = open(filename, 'rw')
print "%s is open.\n" % filename


action = startedit(filename)
print "You would like to: %s" % action
print "Is that correct? [y/n]"

confirm = raw_input(prompt).upper()
if confirm == "Y" or "YES":
    edittype(action, target)
else:
    quit()

target.close()
