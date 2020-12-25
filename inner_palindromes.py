""" A script to find k-lengthed palindromes in a given string"""

def ispal(s: str) -> bool:
    return s[:len(s) // 2] == s[:len(s) // 2 : -1] 


def getpals(s: str, k: int) -> str:
    for i in range(0, len(s) - k + 1):
         if ispal( pal := s[i : i + k] ): yield pal

if __name__ == "__main__":
    s = input('enter string u wanna check for inner palindromes>')
    k = int( input('wanted palindromes length?>') )

    for i in getpals(s, k): print(i)