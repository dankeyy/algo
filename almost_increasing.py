
# 1 2 3 2 4
def almost_increasing_seq(seq: list):
    #allgood = True
    #prev = seq[0]
#
#    for curr in seq[1:]:
#        if prev > curr:
#            if allgood: allgood = not allgood
#
#            else: return not allgood
#
#        else: prev = curr
#        
#    return True
    
    prev = seq[0]
    prevprev = 0
    allgood = True

    for i, curr in enumerate(seq[1:], 1):
        if prev > curr:
            if allgood: 
                allgood = False
                prev = prevprev
            else:
                return False
        else:
             

    return True

if __name__ == "__main__":
    x = [1,3,2,1]
    print(almost_increasing_seq(x))