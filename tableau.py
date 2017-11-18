from fractions import Fraction
from sortedcontainers import SortedDict, SortedSet
from enum import Enum


FeasibleResult = Enum("FeasibleResult", "UNBOUNDED, BOUNDED")


class Tableau():


    def __init__(self, c, A, b, pivot):
        self.nv = len(c)

        # total number of variables, including slack variables
        self.n = len(c) + len(A)
        self.m = len(A)
        self.nb_additional_vars = 0

        nslack = self.n - len(c)

        # include slack variables inside everything
        self.c = c + [0] * nslack
        self.A = [row + [0] * nslack for row in A]
        self.b = b
        self.pivot_rule = pivot

        # all variables are initially set to 0
        self.nonbasis = SortedSet(range(self.n))
        self.basis = SortedSet()

        # used to keep track of which row a basic variable is associated with
        self.rows = SortedDict()

        self.opt = 0
        self.count = 0


    def initialize_basis(self):
        b = self.b
        A = self.A
        n = self.n

        additional = 0
        for k in range(self.m):
            if b[k] < 0:
                additional += 1

        for k in range(self.m):
            A[k] += [0] * additional

            if b[k] < 0:
                for i in range(n):
                    A[k][i] *= -1
                A[k][self.n] = 1
                A[k][self.nv + k] = -1
                b[k] *= -1

                self.basis.add(self.n)
                self.rows[self.n] = k
                self.n += 1

            else:
                s = self.nv + k
                A[k][s] = 1
                self.nonbasis.remove(s)
                self.basis.add(s)
                self.rows[s] = k

        self.nb_additional_vars = additional

        if self.nb_additional_vars > 0:
            next_c = [0] * n + [-1] * additional
        else:
            next_c = None

        return next_c


    def set_objective_vector(self, c):
        self.opt = 0

        for v in self.basis:
            if c[v] == 0:
                continue

            r = self.rows[v]
            for j in range(self.n):
                c[j] -= c[v] * self.A[r][j]
            self.opt -= c[v] * self.b[r]

        self.c = c


    def remove_additional_vars(self):
        d = self.nb_additional_vars
        self.n -= d

        for row in self.A:
            del row[-d:]

        for i in range(self.n, self.n + d):
            self.nonbasis.remove(i)


    def get_entering_candidates(self):
        return [(i, self.c[i]) for i in self.nonbasis if self.c[i] > 0]


    def get_leaving_candidates(self, entering):
        C = []

        for k in self.basis:
            r = self.rows[k]
            if self.A[r][entering] > 0:
                C.append(((k, r), self.b[r] / self.A[r][entering]))

        return C


    def phase(self, verbose):
        if verbose:
            print("The initial tableau is:")
            self.print()

        while True:
            entering_candidates = self.get_entering_candidates()

            if len(entering_candidates) == 0:
                return FeasibleResult.BOUNDED

            entering, _ = self.pivot_rule.pick_entering_var(entering_candidates)
            leaving_candidates = self.get_leaving_candidates(entering)

            if len(leaving_candidates) == 0:
                return FeasibleResult.UNBOUNDED

            (lv, lr), _ = self.pivot_rule.pick_leaving_var(leaving_candidates)

            self.pivot(entering, lv, lr)
            self.count += 1

            if verbose:
                print("The entering variable is x%i" % (entering + 1))
                print("The leaving variable is x%i" % (lv + 1))
                self.print()


    def get_solution(self):
        res = []

        for i in range(self.nv):
            if i in self.nonbasis:
                res.append("x%i = 0" % (i + 1))
            else:
                r = self.rows[i]
                res.append("x%i = %s" % (i + 1, str(self.b[r])))

        return ", ".join(res)


    def pivot(self, entering, lv, lr):
        r = 1 / self.A[lr][entering]

        del self.rows[lv]

        for j in range(self.n):
            self.A[lr][j] *= r
        self.b[lr] *= r

        self.basis.remove(lv)
        self.nonbasis.add(lv)

        for k in self.basis:
            kr = self.rows[k]
            if self.A[kr][entering] != 0:
                r = - self.A[kr][entering]
                for j in range(self.n):
                    self.A[kr][j] += r * self.A[lr][j]
                self.b[kr] += r * self.b[lr]

        r = -self.c[entering]
        for j in range(self.n):
            self.c[j] += r * self.A[lr][j]
        self.opt += r * self.b[lr]

        self.nonbasis.remove(entering)
        self.basis.add(entering)
        self.rows[entering] = lr


    def print(self):
        header = ""
        lines = [""] * self.m

        old_pad = 0
        new_pad = 0

        for j in range(self.n):
            for i in range(self.m):
                lines[i] += " " * (old_pad - len(lines[i])) + str(self.A[i][j]) + "  "
                new_pad = max(new_pad, len(lines[i]))
            header += " " * (old_pad - len(header)) + str(self.c[j]) + "  "
            old_pad = max(new_pad, len(header))

        for i in range(self.m):
            lines[i] += " " * (old_pad - len(lines[i])) + "|  " + str(self.b[i])
            new_pad = max(new_pad, len(lines[i]))
        header += " " * (old_pad - len(header)) + "|  " + str(self.opt)

        print("\n" + header)
        print("-" * (max(len(header), new_pad) + 2))
        for line in lines:
            print(line)
        print()

