import sys
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) < 3:
       sys.exit("This utility requires at least two parameters n and m.")

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    if len(sys.argv) < 4:
        typ = "bounded"
    else:
        typ = sys.argv[3]

    if typ == "bounded":
        v = np.random.randint(10, size=(n, 1))
        A = np.random.randint(-10, 10, size=(m, n))
        b = A.dot(v) + np.random.randint(5, size=(m, 1))
        c = np.random.randint(10, size=(n, 1))

    elif typ == "unbounded" or typ == "infeasible":
        if typ == "infeasible":
            n, m = m, n

        u = np.random.randint(10, size=(n, 1))
        v = np.random.randint(1, 10, size=(n, 1))
        A = np.random.randint(-10, 10, size=(m, n))
        y = A.dot(v)

        for j in range(m):
            if y[j,0] > 0:
                A[j] *= -1

        b = A.dot(u) + np.random.randint(5, size=(m, 1))
        c = v

        if typ == "infeasible":
            n, m = m, n
            c, b = -b, -c
            A = -np.transpose(A)

    else:
        sys.exit("Unknown type of LP problem: %s" % typ)

    print(n)
    print(m)

    print(" ".join(map(str, np.transpose(c)[0])))
    print(" ".join(map(str, np.transpose(b)[0])))

    for row in A:
        print(" ".join(map(str, row)))

