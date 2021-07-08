from src.controllers.genetic_algorithm_controller import GeneticAlgotithmController


def main():
    genetic_algorithm = GeneticAlgotithmController()
    genetic_algorithm.run_genetic_algorithm_to_dixon_price_function()
    genetic_algorithm.run_genetic_algorithm_to_perm_function_d()


if __name__ == "__main__":
    main()