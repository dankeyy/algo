def fizzbuzz(n):
    for i in range(1, n):
        print('fizzbuzz' if i % 15 == 0 else 'buzz' if i % 5 == 0 else 'fizz' if i % 3 == 0  else i)

if __name__ == '__main__':
    fizzbuzz(500)