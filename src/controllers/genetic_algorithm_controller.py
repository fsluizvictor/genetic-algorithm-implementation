from src import config
from src.factory.dixon_price_function_factory import DixonPriceFunctionFactory
from src.factory.perm_function_d_factory import PermFunctionDFactory
from src.services.dixon_price_function_services import DixonPriceFunctionService
from src.services.genetic_algorithms_service import GeneticAlgorithmsService
from src.services.individual_services import IndividualServices
from src.services.perm_function_d_services import PermFunctionDServices


class GeneticAlgotithmController(object):
    def __init__(self):
        self.dixon_price_function_factory = DixonPriceFunctionFactory()
        self.perm_function_d_factory = PermFunctionDFactory()
        self.individual_service = IndividualServices()
        self.genetic_algorithm_service = GeneticAlgorithmsService(self.individual_service)

    def run_genetic_algorithm_to_dixon_price_function(self):
        self.genetic_algorithm_service.execute_to_dixon_price_function(config.AMOUNT_INDIVIDUALS,
                                                                       self.dixon_price_function_factory,
                                                                       config.DIMENSION, config.AMOUNT_STEPS)

    def run_genetic_algorithm_to_perm_function_d(self):
        self.genetic_algorithm_service.execute_to_perm_function_beta(config.AMOUNT_INDIVIDUALS,
                                                                     self.perm_function_d_factory,
                                                                     config.DIMENSION, config.AMOUNT_STEPS)
