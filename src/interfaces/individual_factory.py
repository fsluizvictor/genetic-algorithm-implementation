from abc import ABC, abstractmethod
from typing import List

from src.models.individual import Individual


class IndividualFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_individuals(self, amount_individuals: int, dimension: int) -> List[Individual]:
        pass
