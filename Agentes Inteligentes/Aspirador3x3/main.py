from vacuum import VacuumCleaner
from vacuum import RandonVacuumCleaner
from search import depth_first_graph_search as busca_em_profundidade
from search import breadth_first_graph_search as busca_em_largura
from search import uniform_cost_search as custo_uniforme
from search import depth_limited_search as profundidade_limitada
from search import iterative_deepening_search as busca_interativa
import random


class Presets:
    @staticmethod
    def get_proposed_suggestion():
        return ((0, 1), (0, 1), (0, 1),
                (0, 0), (1, 0), (0, 0),
                (0, 0), (0, 0), (0, 0))

    def probability(self):
        probability = random.sample(range(4), k=1)
        if probability == 1:
            return 1
        return 0
    
    def generate_random_scenario(self):
        aux = list()
        for i in range(9):
            aux.append( (0, self.probability()) )
        
        initial_position = random.sample(range(4), k=1)
        aux[initial_position][0] = 1

        return tuple(aux) 


def print_state(state, title=None):
    if(title != None):
        print("\n {} \n".format(title))
    for index, iterator in enumerate(state):
        if (index+1) % 3 == 0:
            print(iterator)
            continue
        print(iterator, end="")


def print_info(title, initial_state):
    print("-----------------------------------------------------------------")
    print("\n\n-----------------------------------------------------------------")
    print(" " + title)
    print("\nEstado inicial:")
    print_state(initial_state)


def questao3():

    print_info("Busca em profundidade", Presets.get_proposed_suggestion())
    problem = VacuumCleaner(Presets.get_proposed_suggestion())
    print("\nSolução: ", end='')
    print(busca_em_profundidade(problem).solution())
    print("Custo: " + str(problem.custo))
    print_state(busca_em_profundidade(problem).state, "Estado final:")

    print_info("Busca em largura", Presets.get_proposed_suggestion())
    problem = VacuumCleaner(Presets.get_proposed_suggestion())
    print("\nSolução: ", end='')
    print(busca_em_largura(problem).solution())
    print("Custo: " + str(problem.custo))
    print_state(busca_em_largura(problem).state, "Estado final:")

    print_info("Busca de custo uniforme", Presets.get_proposed_suggestion())
    problem = VacuumCleaner(Presets.get_proposed_suggestion())
    print("\nSolução: ", end='')
    print(custo_uniforme(problem).solution())
    print("Custo: " + str(problem.custo))
    print_state(custo_uniforme(problem).state, "Estado final:")

    print_info("Busca em profundidade limitada",
               Presets.get_proposed_suggestion())
    problem = VacuumCleaner(Presets.get_proposed_suggestion())
    print("\nSolução: ", end='')
    print(profundidade_limitada(problem).solution())
    print("Custo: " + str(problem.custo))
    print_state(profundidade_limitada(problem).state, "Estado final:")

    print_info("Busca interativa", Presets.get_proposed_suggestion())
    problem = VacuumCleaner(Presets.get_proposed_suggestion())
    print("\nSolução: ", end='')
    print(busca_interativa(problem).solution())
    print("Custo: " + str(problem.custo))
    print_state(busca_interativa(problem).state, "Estado final:")


def questao4():
    pass


questao3()
print("\n\n\nAgente aleatório\n\n\n")
questao4()
