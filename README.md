## Simplex

Python implementation of the Simplex algorithm, done for the OA course supervised by Nicolas Bousquet at ENS de Lyon.

### Installation

Dependencies:
- `sortedcontainers`: Used to keep a dictionary with ordered keys. 

### Usage

```
simplex.py [-h] [-v] [-p {bland,random,maximum,minimum}] file

positional arguments:
  file                  the input LP problem

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         enable verbose output
  -p {bland,random,maximum,minimum}, --pivot {bland,random,maximum,minimum}
                        select the pivot rule to be used during resolution
                        (default: bland)
```

This information can be obtained by running `python3 simplex.py --help".

The `file` argument must contain some LP problem represented as:

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

### Assignment Notes

#### Pivot Rules
4 different pivot rules where implemented:
- **Bland's rule**. See [here](https://en.wikipedia.org/wiki/Bland's_rule) for an explaination.
- **Maximum coefficient rule**. At each step, we choose the entering variable with the *largest* coefficient in the objective function.
- **Minimum coefficient rule**. At each step, we choose the entering variable with the *smallest* coefficient in the objective function.
- **Random rule**. We pick entering and leaving variables uniformly at random among valid candidates.
