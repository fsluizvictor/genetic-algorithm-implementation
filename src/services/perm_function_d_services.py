from src import config
from src.models.individual import Individual
from src.services.individual_services import IndividualServices


class PermFunctionDServices(IndividualServices):

    def to_rate(self, individual: Individual) -> float:
        outer = 0
        for i in range(len(individual.genes)):
            inner = 0
            for j in range(len(individual.genes)):
                gene = individual.genes[j]
                inner += j.__pow__(i + config.CONSTANT_PERM_FUNCTION_D) * ((gene / j).__pow__(i - 1))
            outer += inner.__pow__(2)

        return outer


