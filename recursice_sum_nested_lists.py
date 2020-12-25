#!/usr/bin/env python3

def deep_sum(item):
    if isinstance(item, int):
        return item

    elif isinstance(item, list) and len(item) == 1:
        return deep_sum(item[0])

    else:
        return deep_sum(item[0]) + deep_sum(item[1:]) 

print(deep_sum([ [ 1,1,1 ], 1, [ 1,[1] ] ]))
