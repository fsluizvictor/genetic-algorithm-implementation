from random import random

from src.models.individual import Individual


class PermFunctionD(Individual):
    def __init__(self, dimension: int):
        super().__init__(dimension)

