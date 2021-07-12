import random
from typing import List


class Individual(object):
    def __init__(self, dimension: int = 2):
        self._rate = 0.0
        self._genes = list()
        self._genes = [random.uniform(-dimension, dimension) for i in range(int(dimension))]
        self._dimension = dimension
        self._is_minimization = True

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate: float):
        self._rate = rate

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, genes: List[float]):
        self._genes = genes

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: int):
        self._dimension = dimension

    @property
    def is_minimization(self):
        return self._is_minimization

    def __eq__(self, other):
        return self._genes == other
