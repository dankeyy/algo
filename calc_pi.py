from decimal import Decimal

""" there are other methods by i went by the Bailey–Borwein–Plouffe formula """

def calc(prec):
    return sum(1/Decimal(16**k) * 
               (Decimal(4)/(8*k+1) - 
                Decimal(2)/(8*k+4) - 
                Decimal(1)/(8*k+5) -
                Decimal(1)/(8*k+6))
                for k in range(prec))


if __name__ == "__main__":
    print(calc(1000))