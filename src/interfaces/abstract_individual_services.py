from abc import ABC, abstractmethod
from typing import Tuple, List

from src.models.individual import Individual


class AbstractIndividualServices(ABC):

    @abstractmethod
    def blx_alfa_crossover(self, first_individual: Individual, second_individual: Individual) -> List[Individual]:
        pass

    @abstractmethod
    def arithmetic_crossover(self, first_individual: Individual, second_individual: Individual) -> List[Individual]:
        pass

    @abstractmethod
    def mutate(self, individual: Individual) -> Individual:
        pass

    @abstractmethod
    def to_rate(self, individual: Individual) -> float:
        pass
