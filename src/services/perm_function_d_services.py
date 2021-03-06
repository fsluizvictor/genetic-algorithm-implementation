from src import config
from src.models.individual import Individual
from src.models.perm_function_d import PermFunctionD
from src.services.individual_services import IndividualServices


class PermFunctionDServices(IndividualServices):

    def to_rate(self, individual: Individual) -> float:
        outer = 0.0
        for i in range(1, len(individual.genes) + 1):
            inner = 0.0
            for j in range(1, len(individual.genes) + 1):
                gene = individual.genes[j - 1]
                inner += ((j ** i) + config.CONSTANT_PERM_FUNCTION_D) * (((gene / j) ** i) - 1)
            outer += inner ** 2

        return outer


