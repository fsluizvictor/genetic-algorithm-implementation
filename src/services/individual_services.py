import random
from typing import Tuple, List

from src import config
from src.interfaces.abstract_individual_services import AbstractIndividualServices
from src.models.individual import Individual


class IndividualServices(AbstractIndividualServices):

    def __init__(self):
        pass

    def mutate(self, individual: Individual) -> Individual:
        pass

    def recombine_arithmetic_crossover(self, first_individual: Individual, second_individual: Individual) -> List[
        Individual]:
        sons = list()
        rate = first_individual.rate

        first_son = Individual(rate)
        second_son = Individual(rate)
        for i in range(rate):
            first_pos_random = random.randint(rate - 1)
            second_pos_random = random.randint(rate - 1)

            first_son.genes[i] = (1 - config.ARITHMETIC_CROSSOVER_COEFFICIENT) * first_individual.genes[
                first_pos_random] + config.ARITHMETIC_CROSSOVER_COEFFICIENT * second_individual.genes[second_pos_random]

            first_pos_random = random.randint(rate - 1)
            second_pos_random = random.randint(rate - 1)

            second_son.genes[i] = (1 - config.ARITHMETIC_CROSSOVER_COEFFICIENT) * second_individual.genes[
                first_pos_random] + config.ARITHMETIC_CROSSOVER_COEFFICIENT * first_individual.genes[second_pos_random]

        return [first_son, second_son]

    def to_rate(self, individual: Individual) -> Individual:
        pass
