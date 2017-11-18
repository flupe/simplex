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


    @staticmethod
    def pick_leaving_var(candidates):
        k = None
        m = inf

        for p, r in candidates:
            # using sortedsets allows us to ignore equalities
            if r < m:
                k = p
                m = r

        return (k, m)


    @staticmethod
    def pick_entering_var(candidates):
        return candidates[0]


class RandomPivot(Pivot):


    @staticmethod
    def pick_leaving_var(candidates):
        return choice(candidates)


    @staticmethod
    def pick_entering_var(candidates):
        return choice(candidates)


class MaximumPivot(BlandPivot):


    @staticmethod
    def pick_entering_var(candidates):
        k = None
        M = -inf

        for p, c in candidates:
            if c > M:
                M = c
                k = p

        return (k, M)
