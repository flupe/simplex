## Simplex

Python implementation of the Simplex algorithm.

Dependencies:
- `sortedcontainers`: Used to keep a dictionary with ordered keys. 

### Usage

```
python3 simplex.py [-h] [-v] [-p {bland,random,custom}] file
```

`file` must contain some LP problem represented as:

```
n
m
c1 c2 ... cn
b1 b2 ... bm
a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn
```

where the goal is to maximize `c.x` under constraints `Ax <= b`, `x >= 0`.
