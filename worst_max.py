import sys
from fractions import Fraction

if __name__ == "__main__":
    if len(sys.argv) < 2:
       sys.exit("This utility requires at least one parameter n.")

    n = int(sys.argv[1])
    m = n
    mu = 4

    A = [[str(2 * mu ** (i - j)) if j < i else "1" if j == i else "0" for j in range(n)] for i in range(m)]
    b = [str(mu ** (2 * i)) for i in range(m)]
    c = [str(mu ** (n - i)) for i in range(1, n + 1)]

    print(n)
    print(m)
    print(" ".join(c))
    print(" ".join(b))
    for row in A:
        print(" ".join(row))

