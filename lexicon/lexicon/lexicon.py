from lexicon import lexicon_words

def convert_number(s):
    try:
        int(s)
        return ('number', int(s))
    except ValueError:
        return s

def scan(s):
    words = s.split()
    sentence = []
    for word in words:
        word = word
        wordtest = word.lower()
        word = convert_number(word)
        for item in lexicon_words.lexiconwords:
            if wordtest in item:
                word = (item[0], word)
            else:
                pass
        if type(word) is str:
            word = ('error', word)
        sentence.append(word)
    return sentence 

s = input('>')
scan(s)
