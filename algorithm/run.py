import cProfile
import random
from deap import base
from deap import creator
from deap import tools
from algorithm.operators import Operators
from model.individual import Individual
from utils.config import Config

random.seed(64)

config = Config(max_demand=10, max_capacity=100, depot_cnt=30, randomize=True)
#config = Config()
operators = Operators(settings=config)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", Individual, fitness=creator.FitnessMin)


def deap_population(deap_type, size):
    my_population = operators.init_population(size)
    return [deap_type(my_individual.routes) for my_individual in my_population]


def deap_evaluation(*args):
    return operators.evaluate_individual(*args),


def deap_crossover(deap_type, child1, child2):
    descendant = operators.crossover(child1, child2)
    return deap_type(descendant.routes)


toolbox = base.Toolbox()
toolbox.register("population", deap_population, creator.Individual)
toolbox.register("evaluate", deap_evaluation)
toolbox.register("mate", deap_crossover, creator.Individual)
toolbox.register("mutate", operators.swap)
toolbox.register("select", tools.selTournament, tournsize=3)


def print_stats(pop):
    fits = [ind.fitness.values[0] for ind in pop]
    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean ** 2) ** 0.5
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)


def main():
    mate_prob, mut_prob, gen_num, pop_size = 0.75, 0.1, 200, 50

    pop = toolbox.population(size=pop_size)

    print("Start of evolution")

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("  Evaluated %i individuals" % len(pop))
    print_stats(pop)

    # Begin the evolution
    for g in range(gen_num):
        print("-- Generation %i --" % g)

        # Select the next generation individuals
        offspring = toolbox.select(pop, 50)
        # Clone the selected individuals
        offspring = list(map(Individual.of, offspring))
        random.shuffle(offspring)

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < mate_prob:
                descendant = toolbox.mate(child1, child2)
                offspring.append(descendant)

        for mutant in offspring:
            if random.random() < mut_prob:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print("  Evaluated %i individuals" % len(invalid_ind))

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        print_stats(pop)

    print("-- End of (successful) evolution --")

    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))


if __name__ == "__main__":
    main()

