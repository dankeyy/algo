from functools import lru_cache

@lru_cache # if py3.9 can just use 'cache'
def cfib(n): # classic recursive fib
    if n <= 2: return 1
    return cfib(n - 1) + cfib(n - 2)


def rfib(n, d={}): # like classical but manually caching using a dict. because y not
    if n in d: return d[n]
    if n <= 2: return 1

    d[n] = rfib(n - 1, d) + rfib(n - 2, d)
    return d[n]


def ifib(n): # iteratively yields all fibs up to n (including). or returns the nth. uncomment whatever
    if n <= 2: return 1
    prev, curr = 0, 1

    for _ in range(n - 1): 
        curr, prev = curr + prev, curr
        # yield curr # if u wanna get all of them
    return curr # if u just want the n-th one


if __name__ == '__main__':
    print(ifib(100000000000))
    # print(rfib(50))
    # print(ifib(50))