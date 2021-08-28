
from collections import Counter
from string import ascii_lowercase as alphabet

def histogram(s):
    words = Counter(s.replace(' ', ''))

    while words:
        hist = []

        for letter in alphabet:

            if found := words.get(letter, None): 
                hist.append('*')
                
                if 1 == found: words.pop(letter)
                else: words[letter] -= 1

            else: hist.append(' ')

        yield ''.join(hist)

        
print(alphabet, *histogram('aba ima'), sep='\n')