def fizzbuzz(n):
    div = lambda x, y: not x % y
    for i in range(1, n):
        # print('fizzbuzz' if i % 15 == 0 else 'buzz' if i % 5 == 0 else 'fizz' if i % 3 == 0  else i)
        print('fizz' * div(i, 3) + 'buzz' * div(i, 5) or i)

if __name__ == '__main__':
    fizzbuzz(500)