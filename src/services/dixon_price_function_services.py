from src.models.individual import Individual
from src.services.individual_services import IndividualServices


class DixonPriceFunctionService(IndividualServices):

    def to_rate(self, individual: Individual) -> float:
        gene_1 = individual.genes[0]
        term_1 = (gene_1 - 1).__pow__(2)

        sum = 0
        for i in range(1, len(individual.genes)):
            gene = individual.genes[i]
            older_gene = individual.genes[i - 1]
            new = i * (float(2 * gene).__pow__(2) - older_gene).__pow__(2)
            sum += new

        return term_1 + sum
