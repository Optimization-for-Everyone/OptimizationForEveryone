from pyharmonysearch import ObjectiveFunctionInterface, harmony_search
import random
import numpy


class ObjectiveFunction(ObjectiveFunctionInterface):

    """
        This is a toy objective function that contains only continuous variables. Here, variable x is fixed at 0.5,
        so only y is allowed to vary.
        Goal:
            maximize -(x^2 + (y+1)^2) + 4
            The maximum is 4 at (0, -1). However, when x is fixed at 0.5, the maximum is 3.75 at (0.5, -1).
        Note that since all variables are continuous, we don't actually need to implement get_index() and get_num_discrete_values().
        Warning: Stochastically solving a linear system is dumb. This is just a toy example.
    """

    def __init__(self, obj_func, lb, ub, dim):
        if not isinstance(lb, list):
            lb = [lb for _ in range(dim)]
            ub = [ub for _ in range(dim)]
        lb = numpy.asarray(lb)
        ub = numpy.asarray(ub)

        self._lower_bounds = lb
        self._upper_bounds = ub
        self._variable = [False, True]

        self.obj_func = obj_func

        # define all input parameters
        self._maximize = False  # do we maximize or minimize?
        self._max_imp = 50000  # maximum number of improvisations
        self._hms = 100  # harmony memory size
        self._hmcr = 0.75  # harmony memory considering rate
        self._par = 0.5  # pitch adjusting rate
        self._mpap = 0.25  # maximum pitch adjustment proportion (new parameter defined in pitch_adjustment()) - used for continuous variables only
        self._mpai = 2  # maximum pitch adjustment index (also defined in pitch_adjustment()) - used for discrete variables only

    def get_fitness(self, vector):
        """
            maximize -(x^2 + (y+1)^2) + 4
            The maximum is 3.75 at (0.5, -1) (remember that x is fixed at 0.5 here).
        """

        return self.obj_func(vector)

    def get_value(self, i, index=None):
        """
            Values are returned uniformly at random in their entire range. Since both parameters are continuous, index can be ignored.
            Note that parameter x is fixed (i.e., self._variable[0] == False). We return 0.5 for that parameter.
        """
        if i == 0:
            return 0.5
        return random.uniform(self._lower_bounds[i], self._upper_bounds[i])

    def get_lower_bound(self, i):
        return self._lower_bounds[i]

    def get_upper_bound(self, i):
        return self._upper_bounds[i]

    def is_variable(self, i):
        return self._variable[i]

    def is_discrete(self, i):
        # all variables are continuous
        return False

    def get_num_parameters(self):
        return len(self._lower_bounds)

    def use_random_seed(self):
        return hasattr(self, '_random_seed') and self._random_seed

    def get_max_imp(self):
        return self._max_imp

    def get_hmcr(self):
        return self._hmcr

    def get_par(self):
        return self._par

    def get_hms(self):
        return self._hms

    def get_mpai(self):
        return self._mpai

    def get_mpap(self):
        return self._mpap

    def maximize(self):
        return self.maximize

def HS(obj_fun, lb = -1000, ub = 1000, dim = 2, SearchAgents_no = 0, num_iterations = 5, num_processes = 2):
    obj_func = ObjectiveFunction(obj_fun, lb = lb, ub = ub, dim = dim)
    results, sol = harmony_search(obj_func, num_processes, num_iterations, obj_fun.__name__)

    print('Elapsed time: {}\nBest harmony: {}\nBest fitness: {}'.format(results.elapsed_time, results.best_harmony, results.best_fitness))
    sol.bestIndividual = results.best_harmony
    sol.convergence = []
    return sol