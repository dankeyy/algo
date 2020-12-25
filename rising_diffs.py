""" A script to filter out items for which there is no differences increase.
    For example if we take [1,2,3,6], the differences will be (1, 1, 3). 
    As seen there is no increment after the second subtraction, therefore the third element will be poped out to output the filtered list: [1,2,6] """

seq = [1, 2, 4, 6, 5, 9, 18]

def rising_diffs(seq):

    def dfilter(seq):
        maxdiff = 0
        
        diff = lambda x: abs(seq[x + 1] - seq[x]) # absolute difference of following elements
        bigger_than_max = lambda diff: diff > maxdiff # bigger diff checker

        yield seq[0]  
        for i in range( len(seq) - 1):
            if bigger_than_max( currdiff := diff(i) ):
                yield seq[i + 1]
                maxdiff = currdiff
            
    return list(dfilter(seq))

if __name__ == '__main__':
    print(rising_diffs(seq))