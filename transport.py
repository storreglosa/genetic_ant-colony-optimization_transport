from random import randrange
from util import constrained_sum_sample_pos
from settings import *


def get_distance_matrix(random=False, max_distance=10):
    size = DEPOT_CNT
    result = EX_DISTANCE_MATRIX
    if random:
        result = [[0 for x in range(size)] for x in range(size)]
        for row in range(size):
            for col in range(row + 1, size):
                result[row][col] = randrange(1, max_distance + 1)
                result[col][row] = result[row][col]
    return result


def get_depots(random=False):
    result = EX_DEPOTS
    if random:
        result = []
        demands = constrained_sum_sample_pos(DEPOT_CNT, MAX_CAPACITY * VEHICLE_CNT)
        for i in range(DEPOT_CNT):
            result.append(Depot(i, demands[i]))
    return result






