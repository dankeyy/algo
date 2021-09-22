"""
Stringy
+======+
Given a string "s" containing non-alphabetic characters, reverse the string so that the position of these non-alphabetic characters is still preserved. 

var s = "abc^defgh==i"
Expected Output:  "ihg^fedcb==a
"""

og = "abc^defgh==i"

def f1(og: str) -> str: # simple procedural solution
    x = list(og)
    start = 0
    end = len(x) -1

    while start != end:
        alpha_start = x[start].isalpha()
        alpha_end = x[end].isalpha()

        if alpha_start == alpha_end: 
                x[start], x[end] = x[end], x[start]
                start += 1
                end -= 1

        elif alpha_start and not alpha_end: end -= 1
        elif not alpha_start and alpha_end: start += 1
    
    return ''.join(x)


def f2(og: str) -> str: # taking advantage of generators, bit easier to comprehend:
    letter = filter(str.isalpha, reversed(og))
    return ''.join(next(letter) if i.isalpha() else i for i in og)


if __name__ == '__main__':
    print(f'{og = }\n{f1(og) = }\n{f2(og) = }')