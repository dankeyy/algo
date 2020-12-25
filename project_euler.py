
def e1(n):
    from itertools import chain
    multiples = lambda x: range(x, n, x)

    return sum( set( chain( multiples(3), multiples(5) ) ) )

"""<-------------------------------------------------------------------------------->"""

def e2(lim): # n = given max curr value 
    
    def evenfib(lim):
        prev, curr = 0, 2
        while curr < lim:
            yield curr
            prev, curr = curr, 4*curr + prev

    return sum(evenfib(lim))

"""<-------------------------------------------------------------------------------->"""

def e3():
   pass 


if __name__ == '__main__':
    print(e1(1000))
    print(e2(4_000_000))
# 1 2 3 5 8 13 ...