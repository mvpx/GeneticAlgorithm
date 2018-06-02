from random import random, choice, randrange
from statistics import mean

N_POPULATION = 20
P_CROSSOVER = 0.9
P_MUTATION = 0.01
N_ITERATIONS = 30


def get_fitness(individual):
    if individual < 0 or individual >= 1024:
        return -1
    if 0 <= individual < 30:
        return 60.0
    elif 30 <= individual < 90:
        return float(individual) + 30.0
    elif 90 <= individual < 120:
        return 120.0
    elif 120 <= individual < 210:
        return -0.83333 * float(individual) + 220
    elif 210 <= individual < 270:
        return 1.75 * float(individual) - 322.5
    elif 270 <= individual < 300:
        return 150.0
    elif 300 <= individual < 360:
        return 2.0 * float(individual) - 450
    elif 360 <= individual < 510:
        return -1.8 * float(individual) + 918
    elif 510 <= individual < 630:
        return 1.5 * float(individual) - 765
    elif 630 <= individual < 720:
        return -1.33333 * float(individual) + 1020
    elif 720 <= individual < 750:
        return 60.0
    elif 750 <= individual < 870:
        return 1.5 * float(individual) - 1065
    elif 870 <= individual < 960:
        return -2.66667 * float(individual) + 2560
    else:
        return 0


def to_decimal(population_b):
    population = []
    for individual in population_b:
        if type(individual) is str:
            population.append(int(individual, 2))
        else:
            population.append(int(individual))
    return population


def to_fitness(population_d):
    population = []
    for individual in population_d:
        population.append(get_fitness(individual))
    return population


def generate(length, size):
    population_b = []
    for _ in range(size):
        population_b.append(''.join(choice('01') for _ in range(length)))
    population_d = to_decimal(population_b)
    population_f = to_fitness(population_d)
    return population_b, population_d, population_f


def select(population_f):
    sum_population_f = sum(population_f)
    random_population_f = randrange(1, int(sum_population_f))
    partial_sum = 0
    for individual_f in population_f:
        partial_sum += individual_f
        if partial_sum >= random_population_f:
            return population_f.index(individual_f)


def validate_length(individual):
    validated = ''
    length = len(individual)
    if length < 10:
        validated += '0' * (10 - length) + individual
    else:
        return individual
    return validated


def crossover(population_b, population_d, population_f, p):
    next_generation_b = []
    for individual in population_d:
        parent1 = validate_length(str(population_b[select(population_f)]))
        if random() < p:
            child = ''
            parent2 = validate_length(str(population_b[select(population_f)]))
            for i in range(10):
                if parent1[i] != parent2[i]:
                    if random() < 0.5:
                        child += parent1[i]
                    else:
                        child += parent2[i]
                else:
                    child += parent1[i]
            next_generation_b.append(child)
        else:
            next_generation_b.append(format(individual, 'b'))
    validated = []
    for individual in next_generation_b:
        validated.append(validate_length(individual))
    next_generation_d = to_decimal(validated)
    next_generation_f = to_fitness(next_generation_d)
    return next_generation_b, next_generation_d, next_generation_f


def mutate(population_b, p):
    population = []
    for individual in population_b:
        child = ''
        for gene in individual:
            child += str(1 - int(gene)) if random() < p else gene
        population.append(child)
    return population


def evolution(generations, length, size, p_mutation, p_crossover):
    population_bin, population_dec, population_fit = generate(length, size)
    for generation in range(generations):
        print(f'{generation+1}. generation')
        print(f'Maximum individual fitness: {max(population_fit)}')
        print(f'Average population fitness: {mean(population_fit)}')
        for individual in population_fit:
            print(f'Individual fitness: {individual}')
        population_bin, population_dec, population_fit = crossover(population_bin, population_dec, population_fit, p_crossover)
        population_bin = mutate(population_bin, p_mutation)


if __name__ == '__main__':
    evolution(N_ITERATIONS, 10, N_POPULATION, P_MUTATION, P_CROSSOVER)








