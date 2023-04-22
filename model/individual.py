import random


class Route(object):
    def __init__(self, route_no=-1, depots=None):
        if not depots:
            depots = []
        self._route_no = route_no
        self._depots = depots

    @staticmethod
    def of(route):
        return Route(route.route_no, list(route.depots))

    @property
    def route_no(self):
        return self._route_no

    @route_no.setter
    def route_no(self, route_no):
        self._route_no = route_no

    @property
    def depots(self):
        return self._depots

    def sum_of_demands(self):
        result = 0
        for depot in self.depots:
            result += depot.demand
        return result

    def calculate_length(self, distance_array):
        result = 0
        first_segment_length = distance_array[0][self.depots[0].depot_no]
        last_segment_length = distance_array[0][self.depots[-1].depot_no]
        result += first_segment_length + last_segment_length
        for curr, nxt in zip(self.depots, self.depots[1:]):
            result += distance_array[curr.depot_no][nxt.depot_no]
        return result

    def insert_depot(self, depot):
        depots_cnt = len(self.depots)
        after_idx = random.randint(0, depots_cnt)
        self.insert_subroute([depot], after_idx)

    def contains_depot(self, depot_no):
        depot_nos = [depot.depot_no for depot in self.depots]
        return depot_no in depot_nos

    def index_of(self, depot_no):
        depot_nos = [depot.depot_no for depot in self.depots]
        return depot_nos.index(depot_no)

    def insert_subroute(self, subroute, after):
        self.depots[after:after] = subroute

    def __eq__(self, other):
        if isinstance(other, Route):
            return self.route_no == other.route_no and self.depots == other.depots
        return False

    def __str__(self):
        return 'Route: {route_no: %d, depots: %s}' % (self.route_no, self.depots)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return unicode(self.__str__())

    def __len__(self):
        return len(self.depots)


class Individual(object):
    def __init__(self, routes=None):
        if not routes:
            routes = []
        self._routes = routes

    @staticmethod
    def of(individual):
        return type(individual)([Route.of(r) for r in individual.routes])

    @property
    def routes(self):
        return self._routes

    def add_depot(self, depot, max_demand_on_route):
        if not self.routes:
            self.routes.append(Route(len(self.routes), []))
        last_route = self.routes[-1]
        if last_route.sum_of_demands() + depot.demand <= max_demand_on_route:
            last_route.depots.append(depot)
        else:
            new_route = Route(len(self.routes), [depot])
            self.routes.append(new_route)

    def add_route(self, depots=None, route=None):
        if depots:
            new_route_no = len(self.routes)
            self.routes.append(Route(new_route_no, depots))
        if route:
            new_route_no = len(self.routes)
            route._route_no = new_route_no
            self.routes.append(route)

    def add_routes(self, routes):
        for route in routes:
            self.add_route(route=route)

    @staticmethod
    def _split_route(route, max_demand_on_route):
        depots = route.depots
        if route.sum_of_demands() <= max_demand_on_route:
            result = [route]
        else:
            result = [Route()]
            for i in range(len(route) - 1, -1, -1):
                current_new_route = result[-1]
                current_depot = depots[i]
                next_demand_sum = current_new_route.sum_of_demands() + current_depot.demand
                if next_demand_sum <= max_demand_on_route:
                    current_new_route.depots.append(current_depot)
                else:
                    result.append(Route(depots=[current_depot]))
        return result

    def check_integrity(self, config):
        if config.debug:
            depots_in_individual = [depot for route in self.routes for depot in route.depots]
            if len(set(depots_in_individual)) != config.depot_cnt - 1:
                raise Exception("Invalid depot count")
            demands = [route.sum_of_demands() for route in self.routes]
            for demand in demands:
                if demand > config.max_capacity:
                    raise Exception("Route exceeds max demand")

    def normalize(self, config):
        max_demand_on_route = config.max_capacity
        new_routes = []
        for route in self.routes:
            if route.sum_of_demands() > max_demand_on_route:
                divided_routes = self._split_route(route, max_demand_on_route)
                new_routes += divided_routes
        filtered_routes = [route for route in self.routes if max_demand_on_route >= route.sum_of_demands() > 0]
        self._routes = new_routes + filtered_routes
        for i in range(len(self.routes)):
            self.routes[i].route_no = i
        self.check_integrity(config)

    def route_with_depot(self, depot):
        for route in self.routes:
            if depot in route.depots:
                return route

    def insert_depot(self, depot):
        route_with_depot = self.route_with_depot(depot)
        route_with_depot.depots.remove(depot)
        if random.random() < (1. / (2. * len(self.routes))):
            self.add_route([depot])
        else:
            random.choice(self.routes).insert_depot(depot)

    def __str__(self):
        return 'Individual: {Routes: %s}' % self.routes

    def __repr__(self):
        return str(self)