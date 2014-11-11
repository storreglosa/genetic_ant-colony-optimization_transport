class Depot(object):
    def __init__(self, depot_no, demand):
        self.depot_no = depot_no
        self.demand = demand

    def __eq__(self, other):
        if isinstance(other, Depot):
            return self.depot_no == other.depot_no and self.demand == other.demand
        return False

    def __hash__(self):
        pass

    def __str__(self):
        return 'Depot: {depot_no: %s; demand: %s}' % (self.depot_no, self.demand)