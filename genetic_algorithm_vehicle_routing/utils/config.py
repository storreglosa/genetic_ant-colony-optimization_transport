from copy import deepcopy
import random
from utils.default_config import *


class Config(object):
    def __init__(self, max_demand=MAX_DEMAND, max_capacity=MAX_CAPACITY, depot_cnt=DEPOT_CNT, randomize=False,
                 debug=False):
        self._max_capacity = deepcopy(max_capacity)
        self._max_demand = deepcopy(max_demand)
        self._depot_cnt = deepcopy(depot_cnt)
        self._depots = self._get_depots(rnd=randomize)
        self._distance_matrix = self._get_distance_matrix(rnd=randomize)
        self._debug = debug

    @property
    def debug(self):
        return self._debug

    @property
    def max_demand(self):
        return self._max_demand

    @property
    def max_capacity(self):
        return self._max_capacity

    @property
    def depot_cnt(self):
        return self._depot_cnt

    @property
    def depots(self):
        return self._depots

    @property
    def distance_matrix(self):
        return self._distance_matrix

    def _get_distance_matrix(self, rnd=False, max_distance=100):
        size = self.depot_cnt
        result = deepcopy(EX_DISTANCE_MATRIX)
        if rnd:
            result = [[0 for x in range(size)] for x in range(size)]
            for row in range(size):
                for col in range(row + 1, size):
                    result[row][col] = random.randrange(1, max_distance + 1)
                    result[col][row] = result[row][col]
        return result

    def _get_depots(self, rnd=False):
        result = deepcopy(EX_DEPOTS)
        if rnd:
            result = []
            for i in range(1, self.depot_cnt):
                result.append(Depot(i, random.randrange(1, self.max_demand + 1)))
        return result


