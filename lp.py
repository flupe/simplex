from tableau import Tableau
from pivot import FeasibleResult

def vect_vars(a):
    return " + ".join(["%i x%i" % (c, i + 1) for i, c in enumerate(a) if c != 0])

class LP:
    def solve(self, verbose = False):
        if verbose:
            print("The input linear program is:\n")
            print("Maximize %s" % vect_vars(self.c))
            print("Such that:")

            for k, row in enumerate(self.A):
                print("\t%s <= %s" % (vect_vars(row), str(self.b[k])))

            print("\t" + ", ".join(["x%i" % (i + 1) for i in range(self.n)]) + " are non-negative\n")

        T = self.T = Tableau(self.c, self.A, self.b, self.pivot)
        phase_one_objective = T.initialize_basis()

        # PHASE 1
        if T.nb_additional_vars > 0:
            if verbose:
                print("=== PHASE 1 ===")
                print("Added %i new positive variables." % T.nb_additional_vars)
                print("Now trying to maximize: %s" % vect_vars(phase_one_objective))

            T.set_objective_vector(phase_one_objective)
            T.phase(verbose)

            if T.opt != 0:
                print("This linear program is INFEASIBLE.")
                self.log()
                return

            else:
                T.remove_additional_vars()
                if verbose:
                    print("Found a basic feasible solution.: %s" % T.get_solution())
                    print("Removed additional variables from the tableau.\n")
                    print("=== PHASE 2 ===")

        # PHASE 2
        T.set_objective_vector(self.c)
        R = T.phase(verbose)

        if R == FeasibleResult.BOUNDED:
            print("This linear problem is FEASIBLE and BOUNDED.")
            print("One optimal solution is: %s" % T.get_solution())
            print("The value of the objective for this solution is: %s" % str(-T.opt))

        else:
            print("This linear problem is FEASIBLE but UNBOUNDED.")

        self.log()

    def log(self):
        print("The number of pivots is: %i" % self.T.count)
        print("The pivot rule used: " + str(self.pivot.__name__))

