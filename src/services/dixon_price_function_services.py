import decimal
from src.models.dixon_price_function import DixonPriceFunction
from src.models.individual import Individual
from src.services.individual_services import IndividualServices


class DixonPriceFunctionService(IndividualServices):

    def to_rate(self, individual: Individual) -> float:
        #individual.genes = list(map(lambda i: 2 ** (-((2 ** i) - 2) / 2 ** i), individual.genes))
        gene_1 = decimal.Decimal(individual.genes[0])
        term_1 = decimal.Decimal((gene_1 - 1) ** 2)

        sum = decimal.Decimal(0)
        for i in range(1, len(individual.genes)):
            gene = decimal.Decimal(individual.genes[i])
            older_gene = decimal.Decimal(individual.genes[i - 1])
            new = i * (2 * (decimal.Decimal(gene) ** 2) - decimal.Decimal(older_gene)) ** 2
            sum += new
        return float(term_1 + sum)


def main():
    ind = DixonPriceFunction(2)
    print(ind.genes)
    ind.genes = [1,2]
    print(ind.genes)
    teste = DixonPriceFunctionService()
    print((teste.to_rate(ind)))


if __name__ == "__main__":
    main()
