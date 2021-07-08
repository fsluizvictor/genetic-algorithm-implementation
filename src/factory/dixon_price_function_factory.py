from typing import List

from src.interfaces.individual_factory import IndividualFactory
from src.models.dixon_price_function import DixonPriceFunction
from src.models.individual import Individual


class DixonPriceFunctionFactory(IndividualFactory):
    
    def get_individuals(self, amount_individuals: int, dimension: int) -> List[Individual]:
        individuals = list()
        individuals = [DixonPriceFunction(dimension) for i in range(amount_individuals)]
        return individuals
