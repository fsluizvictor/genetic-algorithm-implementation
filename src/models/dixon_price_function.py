from random import random

from src.models.individual import Individual


class DixonPriceFunction(Individual):
    def __init__(self, rate: float):
        super().__init__(rate)
        super()._genes = [random.uniform(-10, 10) for i in range(int(rate))]

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, genes: list()):
        self._genes = genes
