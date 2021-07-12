import random
from typing import Tuple, List

from src import config
from src.interfaces.abstract_individual_services import AbstractIndividualServices
from src.models.individual import Individual


class IndividualServices(AbstractIndividualServices):

    def mutate(self, individual: Individual) -> Individual:
        mutate_genes = list()
        for i in range(len(individual.genes)):
            rate_mutate = random.randint(0, 100)
            if rate_mutate > 100:
                mutate_genes.append(individual.genes[i] * random.gauss(0, 0.1) + individual.genes[i])
            else:
                mutate_genes.append(individual.genes[i])

        if individual.genes.__eq__(mutate_genes):
            index_random = random.randint(0, len(mutate_genes) - 1)
            mutate_genes.append(
                mutate_genes[index_random] * random.gauss(0, 0.1) + mutate_genes[index_random])
            mutate_genes.remove(mutate_genes[index_random])

        mutate = Individual(individual.rate)
        mutate.genes = mutate_genes

        return mutate

    def arithmetic_crossover(self, first_individual: Individual, second_individual: Individual) -> List[Individual]:
        dimension = first_individual.dimension

        first_son = Individual(dimension)
        second_son = Individual(dimension)
        for i in range(dimension):
            first_son.genes[i] = (1 - config.ARITHMETIC_CROSSOVER_COEFFICIENT) * first_individual.genes[
                i] + config.ARITHMETIC_CROSSOVER_COEFFICIENT * second_individual.genes[i]

            second_son.genes[i] = (1 - config.ARITHMETIC_CROSSOVER_COEFFICIENT) * second_individual.genes[
                i] + config.ARITHMETIC_CROSSOVER_COEFFICIENT * first_individual.genes[i]

        return [first_son, second_son]

    def blx_alfa_crossover(self, first_individual: Individual, second_individual: Individual) -> List[Individual]:
        dimension = first_individual.dimension

        first_son = Individual(dimension)
        second_son = Individual(dimension)

        for i in range(dimension):
            first_son.genes[i] = first_individual.genes[i] + random.gauss(0, 0.1) * abs(
                first_individual.genes[i] - second_individual.genes[i])

            second_son.genes[i] = second_individual.genes[i] + random.gauss(0, 0.1) * abs(
                first_individual.genes[i] - second_individual.genes[i])
        return [first_son, second_son]

    def to_rate(self, individual: Individual) -> float:
        pass
