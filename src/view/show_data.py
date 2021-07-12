from src.models.individual import Individual
from src.models.perm_function_d import PermFunctionD


class ShowData(object):
    def __init__(self):
        pass

    def show_better_individual_perm_function(self, step_generation: int, individual: Individual):
        print('===============================================')
        print('===============BETTER INDIVIDUAL===============')
        print(f'==============PERM FUNCTION D, BETA===========')
        print('GENERATION : ', step_generation)
        print('Fitness : {:.2f}'.format(individual.rate))
        print('Genes : ')
        print(individual.genes)
        print('===============================================')

    def show_better_individual_dixon_price(self, step_generation: int, individual: Individual):
        print('===============================================')
        print('===============BETTER INDIVIDUAL===============')
        print(f'==============DIXON-PRICE FUNCTION============')
        print('GENERATION : ', step_generation)
        print('Fitness : {:.2f}'.format(individual.rate))
        print('Genes : ')
        print(individual.genes)
        print('===============================================')
