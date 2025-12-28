#!/usr/bin/env python3
from functools import reduce

def sum_equation(L):
    if L:
        L_str = list(map(str, L))
        calc = reduce(lambda x, y: x + " + " + y, L_str)
        res = reduce(lambda x, y: x + y, L, 0)
        return f"{calc} = {res}"
    else:
        return "0 = 0"
def main():
    result = sum_equation([1, 2, 3])
    print(result)

if __name__ == "__main__":
    main()
