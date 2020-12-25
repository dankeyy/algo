
""" A script to remove repeating characters in words """

def picky(sentence):
    for word in sentence.split():
        for i, letter in enumerate(word):
            if letter.lower() not in word[:i].lower():
                yield letter
        yield ' '

def olpicky(sentence): # oneliner picky. Because cause why not
    return ' '.join( ''.join( letter for i, letter in enumerate(word) if letter.lower() not in word[:i].lower()) for word in sentence.split() )

if __name__ == "__main__":
    sentence = 'LoNdoON IS the CAPITAL oF GreaT britain'
    print(''.join( picky(sentence) ))
    print(''.join( olpicky(sentence) ))
