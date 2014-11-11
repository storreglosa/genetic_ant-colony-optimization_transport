from random import randrange, shuffle
from model.individual import Route, Vehicle, Individual

from utils.helper import constrained_sum_sample_pos
from utils.settings import *


def get_distance_matrix(rnd=False, max_distance=10):
    size = DEPOT_CNT
    result = list(EX_DISTANCE_MATRIX)
    if rnd:
        result = [[0 for x in range(size)] for x in range(size)]
        for row in range(size):
            for col in range(row + 1, size):
                result[row][col] = randrange(1, max_distance + 1)
                result[col][row] = result[row][col]
    return result


def get_depots(rnd=False):
    result = list(EX_DEPOTS)
    if rnd:
        result = []
        demands = [randrange(1, MAX_CAPACITY + 1) for i in range(DEPOT_CNT)]
        for i in range(DEPOT_CNT):
            result.append(Depot(i, demands[i]))
    return result


def _generate_individual(depots=None):
    if not depots:
        depots = []
    shuffle(depots)
    current_vehicle = Vehicle(0)
    routes = []
    depots_so_far = []
    while depots:
        current_depot = depots.pop()
        if not current_vehicle.has_capacity(current_depot.demand):
            routes.append(Route(current_vehicle, tuple(depots_so_far)))
            depots_so_far[:] = []
            current_vehicle = current_vehicle.next_vehicle()
        depots_so_far.append(current_depot)
        current_vehicle.deliver(current_depot)
    return Individual(routes)


def init_population(size=100, depots=list(EX_DEPOTS)):
    population = []
    for i in range(size):
        population.append(_generate_individual(depots=depots))
    return population


def crossover():
    pass


def mutation():
    pass


def evaluate_individual():
    pass






