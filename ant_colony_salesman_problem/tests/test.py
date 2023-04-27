import random as rn
import numpy as np
from numpy.random import choice as np_choice
from math import sqrt
import matplotlib.pyplot as plt
import json
from ant_colony_salesman_problem import main

#Presolved TSP Instance
with open("/home/storreglosa/Projects/03_Metaheuristicas_transporte/Genetic_Algoritm_Vehicle_Routing/sample_data/gr120.json", "r") as tsp_data:
    tsp = json.load(tsp_data)

distances = tsp["DistanceMatrix"]
tour_size=tsp["TourSize"]
for i in range(tour_size):
  distances[i][i]=np.inf
distances=np.array(distances)




ant_colony = AntColony(distances, 50, 50, 150, 0.7, alpha=1, beta=1)
shortest_path,log = ant_colony.run()
print ("shortest_path: {}".format(shortest_path))
plt.plot(log)
plt.show()
