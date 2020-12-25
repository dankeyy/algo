#!/usr/bin/env python3

def rec_flattener(item): #"regular", recursion only
    if isinstance(item, int):
        return [item]

    elif isinstance(item, list) and len(item) == 1:
        return rec_flattener(item[0])

    else:
        return rec_flattener(item[0]) + rec_flattener(item[1:])



def gen_flatten(item): # with generator
    if isinstance(item, int):
        yield item

    else:
        for i in item:
            if isinstance(item, list):
                yield from gen_flatten(i)
    
            else:
                yield i


def iterative_flattener(lis): # loops and generators only
    for i in lis:
        if isinstance(i, int):
            yield i # if i is just an int we can yield it

        else: 
            curr = i[0] # handler to yield out every integer 
            left = i[1:] # for leftovers

            while True:
                if isinstance(curr, int):
                    yield curr
                    if left:
                        # moving forward on the sublist
                        curr = left[0]
                        left = left[1:]
                        continue

                if isinstance(curr, list): 
                    if len(curr) != 1:
                        left.insert(0, curr[1:]) #inserting sublist to the beginning of our leftovers
                    curr = curr[0]
                
                else:
                    break #curr is not a list, but an int we've yielded. left is empty. we can safetly break


def simpler_flatten(data):
    i = 0
    result = data.copy()
    while i < len(result):
        if isinstance(result[i], list):
            result[i:i + 1] = result[i]
        else:
            i += 1
    return result     



if __name__ == '__main__':

    lis1 = [ [ 1,[2], 3 ], 4, [ 5,[6] ] ]
    lis2 = [1, [[2, 3], [[4]]], [5, [ 6, [[7]] ], [[8], [9, [10]]]]]

    print(f'original list = {lis2}')
    print(f'flattened list = {simpler_flatten(lis1)}')

    # print(reg_flatten(lis1))

    # gen_handler = lambda x: list(gen_flatten(x))
    # print(gen_handler(lis1))
    #print(iterative_flatten(lis1))