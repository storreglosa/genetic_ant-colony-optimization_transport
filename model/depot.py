class Depot(object):
    def __init__(self, depot_no, demand):
        self._depot_no = depot_no
        self._demand = demand

    @property
    def depot_no(self):
        return self._depot_no

    @property
    def demand(self):
        return self._demand

    def get_closest_depot_no(self, distances):
        all_distances = distances[self.depot_no]
        # ignoring distance to itself
        second_closest_distance = sorted(all_distances)[1]
        return all_distances.index(second_closest_distance)

    def __eq__(self, other):
        if isinstance(other, Depot):
            return self.depot_no == other.depot_no and self.demand == other.demand
        return False

    def __hash__(self):
        return hash((self.depot_no, self.demand))

    def __str__(self):
        return 'Depot: {depot_no: %s; demand: %s}' % (self.depot_no, self.demand)

    def __repr__(self):
        return str(self)