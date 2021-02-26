characters = ('I', 'V', 'X', 'L', 'C', 'D', 'M')[::-1]
numeric_value = (1,5,10,50,100,500,1000)[::-1]
convert = {k:v for k, v in zip(numeric_value, characters)}

def gimmenumber(n):
    i = 0
    roman =''
    while n:
        for x in range(n // numeric_value[i]):
            roman += characters[i]
            n -= numeric_value[i]
        i += 1

    return roman

print(gimmenumber(23))