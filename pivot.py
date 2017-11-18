from random import choice
from math import inf


class Pivot:
    @staticmethod
    def pick_leaving_var(candidates):
        raise NotImplementedError

    @staticmethod
    def pick_entering_var(candidates):
        raise NotImplementedError


class BlandPivot(Pivot):
    def pick_leaving_var(candidates):
        return candidates[0]

    def pick_entering_var(candidates):
        return candidates[0]


class RandomPivot(Pivot):
    def pick_leaving_var(candidates):
        return choice(candidates)

    def pick_entering_var(candidates):
        return choice(candidates)


class MaximumPivot(BlandPivot):
    def pick_entering_var(candidates):
        k = None
        M = -inf

        for p, c in candidates:
            if c > M:
                M = c
                k = p

        return (k, M)

class MinimumPivot(BlandPivot):
    def pick_entering_var(candidates):
        k = None
        m = inf

        for p, c in candidates:
            if c < m:
                m = c
                k = p

        return (k, m)
