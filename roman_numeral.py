characters    = ('M',  'D', 'C', 'L', 'X', 'V', 'I') 
numeric_value = (1000, 500, 100,  50,  10,  5,   1 ) 

def gimmenumber(n):
    i = 0
    roman = ''

    while n:
        for x in range(n // numeric_value[i]):
            roman += characters[i]
            n -= numeric_value[i]
        i += 1

    return roman

print(gimmenumber(12345))