from unittest import TestCase
from algorithm.operators import Operators
from model.depot import Depot
from model.individual import Route, Individual

__author__ = 'Marek'


class TestOperators(TestCase):
    def setUp(self):
        self.operators = Operators()
        self.depots = self.operators.settings.depots

    def test_inversion(self):
        depots = self.depots[0:3]
        route = Route(0, list(depots))
        individual = Individual([route])
        Operators.inversion(individual)
        self.assertItemsEqual(depots, route.depots)

    def test_insertion(self):
        depots = self.depots
        route = Route(0, list(depots))
        individual = Individual([route])
        individual.normalize(self.operators.settings.max_demand)
        self.operators.insertion(individual)