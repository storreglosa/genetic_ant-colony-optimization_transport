class Route(object):
    def __init__(self, route_no, depots):
        self._route_no = route_no
        self._depots = depots

    @property
    def route_no(self):
        return self._route_no

    @property
    def depots(self):
        return self._depots

    def sum_of_demands(self):
        return sum(depot.demand for depot in self.depots)

    def calculate_length(self, distance_array):
        result = 0
        first_segment_length = distance_array[0][self.depots[0].depot_no]
        last_segment_length = distance_array[0][self.depots[-1].depot_no]
        result += first_segment_length + last_segment_length
        for curr, nxt in zip(self.depots, self.depots[1:]):
            result += distance_array[curr.depot_no][nxt.depot_no]
        return result

    def contains_depot(self, depot_no):
        depot_nos = [depot.depot_no for depot in self.depots]
        return depot_no in depot_nos

    def index_of(self, depot_no):
        depot_nos = [depot.depot_no for depot in self.depots]
        return depot_nos.index(depot_no)

    def insert_subroute(self, subroute, after):
        self.depots[after:after] = subroute

    def __str__(self):
        return 'Route: {route_no: %d, depots: %s}' % (self.route_no, self.depots)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return unicode(self.__str__())


class Individual(object):
    def __init__(self, routes=None):
        if not routes:
            routes = []
        self._routes = routes

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

    def normalize(self, max_demand_on_route):
        all_depots = [depot for route in self.routes for depot in route.depots]
        unique_depots = set()
        for depo in all_depots:
             unique_depots.add(depo)
        self._routes = []
        for depot in unique_depots:
            self.add_depot(depot, max_demand_on_route)




    def __str__(self):
        return 'Individual: {Routes: %s}' % self.routes

    def __repr__(self):
        return str(self)
