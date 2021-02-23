from fractions import Fraction
from functools import reduce
#https://www.youtube.com/watch?v=hUes6y2b--0&list=PLWVmTKtJ7GyBN27dZVVeqppl0RMVzsENP&index=19
#https://docs.python.org/3/library/fractions.html
def product(fracs):
    t = Fraction(reduce(lambda x,y : x * y, fracs))
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)