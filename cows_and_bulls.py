from random import sample
from string import digits

# https://en.wikipedia.org/wiki/Bulls_and_Cows

def main():
    random_num = ''.join(sample(digits, 4))
    bulls = 0

    while bulls != 4:
        bulls = cows = 0
        guess = input() # trust worthy 4 distinct digit number, im not gonna bother checking
         
        for user_digit, random_digit in zip(guess, random_num):
            if user_digit == random_digit: bulls += 1
            elif user_digit in random_num: cows += 1

        print(f"{bulls = }, {cows = }")

    print('u win')

main()