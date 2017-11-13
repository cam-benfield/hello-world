stuff = raw_input('> ')
words = stuff.split()

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return none
    
