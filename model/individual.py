from utils.settings import MAX_CAPACITY


class Vehicle(object):
    def __init__(self, vehicle_no):
        self.vehicle_no = vehicle_no
        self.current_capacity = MAX_CAPACITY

    def deliver(self, depot):
        if self.has_capacity(depot.demand):
            self.current_capacity -= depot.demand

    def has_capacity(self, amount):
        return self.current_capacity >= amount

    def next_vehicle(self):
        return Vehicle(self.vehicle_no + 1)

    def __str__(self):
        return 'Vehicle{vehicle_no: %d; current_capacity: %d}' % (self.vehicle_no, self.current_capacity)




class Route(object):
    def __init__(self, vehicle, depots=None):
        if not depots:
            depots = []
        self.vehicle = vehicle
        self.depots = depots

    def __str__(self):
        return 'Route: {vehicle: %s; depots: %s}' % (self.vehicle, self.depots)


class Individual(object):
    def __init__(self, routes):
        self.routes = routes

    def __str__(self):
        return 'Individual: {Routes: %s}' % self.routes
