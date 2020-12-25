#!/usr/bin/env python3
def valid_parentheses(string):
    opening_brackets = closing_brackets = 0
    
    for i in string:
        if i == '(': opening_brackets += 1
        elif i == ')': closing_brackets += 1
        
        if closing_brackets > opening_brackets: return False

    return opening_brackets == closing_brackets


if __name__ == '__main__':
    print('Should be True, function returns ', valid_parentheses('()()()()'))
    print('Should be False, function returns ', valid_parentheses('()())))'))
    print('Should be False, function returns ', valid_parentheses('()())))'))
    print('Should be True, function returns ', valid_parentheses('(())(()(())())()'))
    print('Should be False, function returns ', valid_parentheses('))))))'))
    print('Should be False, function returns ', valid_parentheses('(((((('))