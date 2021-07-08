from random import random
from typing import List

from src.models.individual import Individual


class DixonPriceFunction(Individual):
    def __init__(self, dimension: int):
        super().__init__(dimension)
        super()._genes = [random.uniform(-10, 10) for i in range(int(dimension))]

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, genes: List[float]):
        self._genes = genes
