# Simplex

Python implementation of the Simplex algorithm, done for the OA course supervised by Nicolas Bousquet at ENS de Lyon.

## Installation

Dependencies:
- `sortedcontainers`: Used to keep a dictionary with ordered keys. 

## Usage

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

## Assignment Notes

### Pivot Rules
4 different pivot rules where implemented:
- **Bland's rule**. See [here](https://en.wikipedia.org/wiki/Bland's_rule) for an explaination.
- **Maximum coefficient rule**. At each step, we choose the entering variable with the *largest* coefficient in the objective function.
- **Minimum coefficient rule**. At each step, we choose the entering variable with the *smallest* coefficient in the objective function.
- **Random rule**. We pick entering and leaving variables uniformly at random among valid candidates.

### Test Examples

#### From exercise sheets

Three problems have been taken from exercise sheets and formatted as valid input files for our solver.
- `tests/lumberjack`.
- `tests/busdrivers`.
  The **Bus drivers** problem consists of finding the *minimum amount* of bus drivers to hire when each driver works for 5 consecutive days and you need 17 drivers working on Mondays, 21 on Tuesdays, 15 on Wednesdays, 20 on Thursdays, 23 on Fridays, 15 on Saturdays and 9 on Sundays.
  We can express this as a LP problem by defining variables `x_i`: *number of drivers hired to start working on the ith day of the week*.
  Then for each day `i`, we need the sufficient amount of drivers still working that day.
  We end up with the following constraints:
  - `x_1 + x_4 + x_5 + x_6 + x_7 >= 17`
  - `x_1 + x_2 + x_5 + x_6 + x_7 >= 21`
  - `x_1 + x_2 + x_3 + x_6 + x_7 >= 15`
  - `x_1 + x_2 + x_3 + x_4 + x_7 >= 20`
  - `x_1 + x_2 + x_3 + x_4 + x_5 >= 23`
  - `x_2 + x_3 + x_4 + x_5 + x_6 >= 15`
  - `x_3 + x_4 + x_5 + x_6 + x_7 >= 9`
  with the aim of minimizing `x_1 + ... + x_n`.
  Once expressed as a maximization problem in the defined format, running our solver gives us an optimal minimum amount of `73/3` drivers to hire. Turning this into an integer optimal solution, we get `25` drivers.

- `tests/lumberjack`.
