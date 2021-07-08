from typing import List

from src.interfaces.individual_factory import IndividualFactory
from src.models.individual import Individual
from src.models.perm_function_d import PermFunctionD


class PermFunctionDFactory(IndividualFactory):

    def get_individuals(self, amount_individuals: int, dimension: int) -> List[Individual]:
        individuals = list()
        individuals = [PermFunctionD(dimension) for i in range(amount_individuals)]
        return individuals
