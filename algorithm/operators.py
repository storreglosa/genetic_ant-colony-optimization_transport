from copy import deepcopy
import random
from model.individual import Route, Individual
from utils.config import Config


class Operators(object):
    def __init__(self, settings=Config()):
        self._settings = settings

    @property
    def settings(self):
        return self._settings

    def _generate_individual(self):
        depots = self.settings.depots
        random.shuffle(depots)
        result = Individual()
        for depot in depots:
            result.add_depot(depot, self.settings.max_capacity)
        return result

    def _generate_individual2(self):
        depots = list(self.settings.depots)
        random.shuffle(depots)
        result = Individual()
        i = 0
        while depots:
            k = random.randrange(1, len(depots) + 1)
            result.routes.append(Route(i, depots[0:k]))
            del depots[0:k]
            i += 1
        return result

    def init_population(self, size=100):
        population = []
        for i in range(size):
            population.append(self._generate_individual())
        return population

    def init_population2(self, size=100):
        population = []
        for i in range(size):
            population.append(self._generate_individual2())
        return population

    def evaluate_individual(self, individual):
        distance_matrix = self.settings.distance_matrix
        total_distance = 0
        for route in individual.routes:
            total_distance += route.calculate_length(distance_matrix)
        return total_distance

    @staticmethod
    def _get_random_subroute(individual):
        random_route = random.choice(individual.routes).depots
        random_route_len = len(random_route)
        if random_route_len <= 1:
            return random_route
        end_idx, start_idx = Operators._get_random_subroute_indices(random_route_len)
        return random_route[start_idx:end_idx]

    def _insert_subroute(self, subroute, individual):
        distances = self.settings.distance_matrix
        first_depot_of_subroute = subroute[0]
        closest_depot_no = first_depot_of_subroute.get_closest_depot_no(distances)
        for route_idx in xrange(len(individual.routes)):
            current_route = individual.routes[route_idx]
            if current_route.contains_depot(closest_depot_no):
                current_route.insert_subroute(subroute, after=closest_depot_no)

    @staticmethod
    def _get_random_subroute_indices(random_route_len):
        if random_route_len == 1:
            return 0, 1
        start_idx = random.randrange(0, random_route_len - 1)
        end_idx = random.randrange(start_idx + 1, random_route_len + 1)
        return end_idx, start_idx

    def crossover(self, first_individual, second_individual):
        descendant = Individual.of(first_individual)
        subroute = self._get_random_subroute(second_individual)
        self._insert_subroute(subroute, descendant)
        descendant.normalize(self.settings)
        return descendant

    def swap(self, individual):
        routes = individual.routes
        first_route_idx = random.randrange(0, len(routes))
        first_dept_idx = random.randrange(0, len(routes[first_route_idx].depots))

        second_route_idx = random.randrange(0, len(routes))
        second_dept_idx = random.randrange(0, len(routes[second_route_idx].depots))

        first = routes[first_route_idx].depots[first_dept_idx]
        routes[first_route_idx].depots[first_dept_idx] = routes[second_route_idx].depots[
            second_dept_idx]
        routes[second_route_idx].depots[second_dept_idx] = first
        individual.normalize(self.settings)

    def inversion(self, individual):
        random_route = random.choice(individual.routes).depots
        random_route_len = len(random_route)
        if random_route_len > 1:
            end_idx, start_idx = Operators._get_random_subroute_indices(random_route_len)
            random_route[start_idx:end_idx] = reversed(random_route[start_idx:end_idx])
        individual.normalize(self.settings)

    def insertion(self, individual):
        depot_to_insert = random.choice(self.settings.depots)
        individual.insert_depot(depot_to_insert)
        individual.normalize(self.settings)

    def displacement(self, individual):
        route_to_get_subroute_from = random.choice(individual.routes)
        route_to_insert_subroute_to = random.choice(individual.routes)
        start_idx, end_idx = self._get_random_subroute_indices(len(route_to_get_subroute_from))
        subroute = route_to_get_subroute_from.depots[start_idx:end_idx]
        after = random.randrange(0, len(route_to_insert_subroute_to))
        route_to_insert_subroute_to.insert_subroute(subroute,
                                                    after=after)
        del route_to_get_subroute_from.depots[start_idx:end_idx]
        individual.normalize(self.settings)





