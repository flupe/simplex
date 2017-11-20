from fractions import Fraction
import argparse as ap

import pivot
from lp import LP

if __name__ == "__main__":
    pivots = {
        "bland": pivot.BlandRule,
        "random": pivot.RandomRule,
        "largest": pivot.LargestCoefficientRule,
        "smallest": pivot.SmallestCoefficientRule,
        "maximum": pivot.MaximumIncreaseRule
    }

    parser = ap.ArgumentParser(
        description = "A Python implementation of the Simplex Algorithm."
    )

    parser.add_argument("-v", "--verbose", action="store_true",
            help="enable verbose output")

    parser.add_argument("-p", "--pivot", default="bland", choices=pivots.keys(),
            help="select the pivot rule to be used during resolution (default: bland)")

    parser.add_argument("file",
            help="the input LP problem")

    inputs = parser.parse_args()

    with open(inputs.file, "r") as data:

        def parse_fractionals(l):
            return list(map(Fraction, l.split()))

        lp = LP()

        lp.n = int(data.readline())
        lp.m = int(data.readline())

        # equation we wish to maximize
        lp.c = parse_fractionals(data.readline())

        # bounds
        lp.b = parse_fractionals(data.readline())

        # constraint matrix
        lp.A = list(map(parse_fractionals, data.readlines()))
        lp.pivot = pivots[inputs.pivot]

        lp.solve(inputs.verbose)
