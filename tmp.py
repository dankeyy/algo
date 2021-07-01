
def depth(x: str) -> int:
    maximum = 0
    count = 0

    for i in x:
        if i == '(': 
            count += 1
            if count > maximum: 
                maximum = count
    
        elif i == ')': 
            count -= 1

    return maximum

print(depth("((()(())))"))