from typing import List

from src import config
from src.models.individual import Individual


class GeneticAlgorithmsService(object):
    def __init__(self):
        pass

    def execute(self, amount_steps: int, amount_individuals: int):
        initial_population = list()
        for i in range(amount_individuals):
            initial_population = self.__generate_initial_population(amount_individuals)

        for s in range(amount_steps):
            sons_population = self.__generate_sons(initial_population)
            mutants_population = self.__generate_mutantes(initial_population)

            all_population = list()
            all_population.extend(initial_population)
            all_population.extend(sons_population)
            all_population.extend(mutants_population)

            all_population = self.__recalculing_fitnes(all_population)

            selected_individuals = self.__selection(all_population, config.AMOUNT_INDIVIDUALS_FOR_ROULETTE,
                                                    config.AMOUNT_INDIVIDUALS_FOR_ELISTISM)
            self.__get_better_individual(selected_individuals)

    def __selection(self, individuals_population: List[Individual], amount_individuals_for_roulette: int,
                    amount_individuals_for_elitism: int) -> List[Individual]:
        pass

    def __generate_initial_population(self, amount_individuals: int) -> List[Individual]:
        pass

    def __generate_sons(self, initial_population: List[Individual]) -> List[Individual]:
        pass

    def __generate_mutantes(self, initial_population: List[Individual]) -> List[Individual]:
        pass

    def __recalculing_fitnes(self, individuals: List[Individual]) -> List[Individual]:
        pass

    def __get_better_individual(self, individuals: List[Individual]):
        pass
