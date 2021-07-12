from random import random

from src.models.individual import Individual


class PermFunctionD(Individual):
    def __init__(self, rate: float):
        super().__init__(rate)

