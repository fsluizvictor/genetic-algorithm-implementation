from abc import ABC, abstractmethod
from typing import Tuple

from src.models.individual import Individual


class Individual_Services(ABC):


    @abstractmethod
    def recombine(self, first_individual: Individual, second_individual: Individual) -> Tuple[Individual, Individual]:
        pass

    @abstractmethod
    def mutate(self, individual: Individual) -> Individual:
        pass

    @abstractmethod
    def to_rate(self, individual: Individual) -> Individual:
        pass
