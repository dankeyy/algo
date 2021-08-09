
from itertools import cycle, islice
from operator import concat

div = lambda x, y: not x % y

def fb1(n):
    for i in range(1, n):
        print('fizz' * div(i, 3) + 'buzz' * div(i, 5) or i)

def fb2(n):
    for i in islice(
            (concat(*v) or i
                for i, v in enumerate(
                    zip(
                        cycle(("", "", "fizz")), 
                        cycle(("", "", "", "", "buzz"))
                    ), 1
                )
            ), n
    ): print(i)



if __name__ == '__main__':
    fb1(100)