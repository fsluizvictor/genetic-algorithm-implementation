from random import random


class Individual(object):
    def __init__(self, rate: float):
        self._rate = rate
        self._genes = list()
        self._genes = [random.uniform(-rate, rate) for i in range(int(rate))]


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
    def genes(self, genes: list()):
        self._genes = genes
