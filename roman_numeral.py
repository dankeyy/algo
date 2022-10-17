numeric = (1000, 900, 500, 400,  100,  90,  50,  40,   10,   9,    5,   4,    1 )
chars   = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

def roman(n):
    return next(
        (l + roman(n-c) for c, l in zip(numeric, chars) if c <= n),
        ''
    )

print(roman(1234))
