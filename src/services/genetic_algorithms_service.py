import operator
import random
from typing import List

from src import config
from src.interfaces.individual_factory import IndividualFactory
from src.models.individual import Individual
from src.services.individual_services import IndividualServices


class GeneticAlgorithmsService(object):
    def __init__(self, individual_service: IndividualServices):
        self.individual_service = individual_service

    def execute_to_dixon_price_function(self, amount_individuals: int = config.AMOUNT_INDIVIDUALS,
                                        individual_factory: IndividualFactory = None,
                                        dimension: int = config.DIMENSION, amount_steps: int = config.AMOUNT_STEPS):
        self.__execute(
            self.__generate_initial_population_dixon_price_function(amount_individuals, individual_factory, dimension),
            amount_steps)

    def execute_to_perm_function_beta(self, amount_individuals: int = config.AMOUNT_INDIVIDUALS,
                                      individual_factory: IndividualFactory = None,
                                      dimension: int = config.DIMENSION, amount_steps: int = config.AMOUNT_STEPS):

        self.__execute(
            self.__generate_initial_population_perm_function_d(amount_individuals, individual_factory, dimension),
            amount_steps)

    def __execute(self, initial_population: List[Individual], amount_steps: int):
        for s in range(amount_steps):
            sons_population = self.__generate_sons(initial_population)
            mutants_population = self.__generate_mutantes(initial_population)

            all_population = list()
            all_population.extend(initial_population)
            all_population.extend(sons_population)
            all_population.extend(mutants_population)

            selected_individuals = self.__selection(all_population, config.AMOUNT_INDIVIDUALS_FOR_ROULETTE,
                                                    config.AMOUNT_INDIVIDUALS_FOR_ELISTISM)
            self.__get_better_individual(selected_individuals)

    def __selection(self, individuals_population: List[Individual], amount_individuals_for_roulette: int,
                    amount_individuals_for_elitism: int) -> List[Individual]:
        elitism_individuals = self.__elitism(individuals_population, amount_individuals_for_elitism)

        for i in range(len(elitism_individuals)):
            individuals_population.remove(elitism_individuals[i])

        individuals_roulette = self.__addited_roulette(individuals_population, amount_individuals_for_roulette)

        individuals_selected = list()
        individuals_selected.extend(elitism_individuals)
        individuals_selected.extend(individuals_roulette)

        return individuals_selected

    def __generate_initial_population_dixon_price_function(self, amount_individuals: int,
                                                           individual_factory: IndividualFactory, dimension: int) -> \
            List[Individual]:

        return individual_factory.get_individuals(amount_individuals, dimension)

    def __generate_initial_population_perm_function_d(self, amount_individuals: int,
                                                      individual_factory: IndividualFactory, dimension: int) -> List[
        Individual]:

        return individual_factory.get_individuals(amount_individuals, dimension)

    def __generate_sons(self, initial_population: List[Individual]) -> List[Individual]:
        sons = list()
        for i in range(0, len(initial_population) - 2, 2):
            for j in range(1, len(initial_population) - 1, 2):
                sons.extend(self.individual_service.arithmetic_crossover(initial_population[i], initial_population[j]))
        return sons

    def __generate_mutantes(self, initial_population: List[Individual]) -> List[Individual]:
        mutants = list()
        for i in range(len(initial_population)):
            mutant = self.individual_service.mutate(initial_population[i])
            mutants.append(mutant)
        return mutants

    def __get_better_individual(self, individuals: List[Individual]):
        pass

    def __elitism(self, individuals_population: List[Individual], amount_elitism: int) -> List[Individual]:
        elitism_individuals = list()
        if individuals_population[0].is_minimization:
            individuals_population.sort(key=operator.attrgetter('rate'))
            for i in range(amount_elitism):
                elitism_individuals.append(individuals_population[i])
        return elitism_individuals

    def __addited_roulette(self, individuals_population: List[Individual], amount_individual: int) -> List[Individual]:
        new_rates = list()
        for i in range(len(individuals_population)):
            if individuals_population[i].rate > 0:
                new_rates.append(1 / individuals_population[i].rate)

        individuals_selected = list()

        for i in range(amount_individual):
            sum_rate = 0.0
            for s in range(len(new_rates)):
                sum_rate += new_rates[s]
            random_rate = random.uniform(0.0, sum_rate)
            aux_sum_rate = 0.0

            for j in range(len(individuals_population)):
                aux_sum_rate += individuals_population[j].rate
                if aux_sum_rate >= random_rate:
                    individual = individuals_population[j]
                    individuals_selected.append(individual)
                    individuals_population.remove(individual)
                    break

        return individuals_selected
