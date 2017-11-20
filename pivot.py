from random import choice
from math import inf
from enum import Enum

FeasibleResult = Enum("FeasibleResult", "UNBOUNDED, BOUNDED, UNKNOWN")

class PivotRule:
    @staticmethod
    def pick_leaving_and_entering_vars(tableau):
        raise NotImplementedError

class TwoStepRule(PivotRule):
    @staticmethod
    def pick_entering_var(candidates):
        raise NotImplementedError

    @staticmethod
    def pick_leaving_var(candidates):
        raise NotImplementedError

    @classmethod
    def pick_leaving_and_entering_vars(C, tableau):
        entering_candidates = tableau.get_entering_candidates()

        if len(entering_candidates) == 0:
            return FeasibleResult.BOUNDED, None, None

        entering, _ = C.pick_entering_var(entering_candidates)

        leaving_candidates = tableau.get_leaving_candidates(entering)

        if len(leaving_candidates) == 0:
            return FeasibleResult.UNBOUNDED, None, None

        leaving = C.pick_leaving_var(leaving_candidates)

        return FeasibleResult.UNKNOWN, entering, leaving


class BlandRule(TwoStepRule):
    def pick_entering_var(candidates):
        return candidates[0]

    def pick_leaving_var(candidates):
        return candidates[0]


class RandomRule(TwoStepRule):
    def pick_entering_var(candidates):
        return choice(candidates)

    def pick_leaving_var(candidates):
        return choice(candidates)


class LargestCoefficientRule(TwoStepRule):
    def pick_entering_var(candidates):
        k = None
        M = -inf

        for p, c in candidates:
            if c > M:
                M = c
                k = p

        return (k, M)

    def pick_leaving_var(candidates):
        return candidates[0]


class SmallestCoefficientRule(TwoStepRule):
    def pick_entering_var(candidates):
        k = None
        m = inf

        for p, c in candidates:
            if c < m:
                m = c
                k = p

        return (k, m)

    def pick_leaving_var(candidates):
        return candidates[0]


class MaximumIncreaseRule(PivotRule):
    def pick_leaving_and_entering_vars(tableau):
        entering_candidates = tableau.get_entering_candidates()

        if len(entering_candidates) == 0:
            return FeasibleResult.BOUNDED, None, None

        e = -1
        l = -1
        m = -inf

        for ec, ce  in entering_candidates:
            lcs = tableau.get_leaving_candidates(ec)

            if len(lcs) == 0:
                continue

            lc = lcs[0]

            r = tableau.rows[lc]
            inc = ce * tableau.b[r] / tableau.A[r][ec]

            if inc > m:
                m = inc
                e = ec
                l = lc

        if l == -1:
            return FeasibleResult.UNBOUNDED, None, None

        return FeasibleResult.UNKNOWN, e, l

