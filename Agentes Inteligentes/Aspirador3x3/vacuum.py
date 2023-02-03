from turtle import position
from search import Problem
import random


class VacuumCleaner(Problem):

    def __init__(self, initial_state):
        self.custo = 0
        super().__init__(initial_state, self.__goal_generator())

    # Gerador de todos os estados finais possíveis.
    def __goal_generator(self):
        list_goal = list()
        list_aux = list()

        for i in range(9):
            for j in range(9):
                if i == j:
                    list_aux.append((1, 0))
                    continue
                list_aux.append((0, 0))
            list_goal.append(tuple(list_aux))
            list_aux = []
        return tuple(list_goal)

    def __find_index_vacuum(self, state):
        for index, iterator in enumerate(state):
            if iterator[0] == 1:
                return index

    def actions(self, state):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SUCK']
        index_vacuum = self.__find_index_vacuum(state)

        if state[index_vacuum][1] == 1:
            return ['SUCK']

        if index_vacuum % 3 == 0:
            possible_actions.remove('LEFT')
        if index_vacuum < 3:
            possible_actions.remove('UP')
        if index_vacuum % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_vacuum > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        index_vacuum = self.__find_index_vacuum(state)
        new_state = list(state)

        if action == "SUCK":
            new_state[index_vacuum] = (1, 0)
            return tuple(new_state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = index_vacuum + delta[action]
        new_state[index_vacuum] = (0, 0)
        new_state[neighbor] = (1, new_state[neighbor][1])
        return tuple(new_state)

    def goal_test(self, state):
        return state in self.goal

    def path_cost(self, c, state1, action, state2):
        if action == 'SUCK':
            self.custo = c + 1
            return c + 1
        self.custo = c + 2
        return c + 2


class RandonVacuumCleaner:
    def __init__(self, max_range, initial_position) -> None:
        self.position = initial_position
        self.max_range = max_range
        self.goa = self.__goal_generator()

    def random_position(self):
        random.seed(8)
        return random.sample(range(self.max_range), k=1)

    def movement(self, state):
        next = self.position
        while next == position:
            next = self.random_position()

        state[position][0] = 0
        state[next][0] = 1

    def check_dirt(self, state):
        if state[self.position][1] == 1:
            state[self.position][1] = 0
            return
        self.movement(state)

    def __goal_generator(self):
        list_goal = list()
        list_aux = list()

        for i in range(9):
            for j in range(9):
                if i == j:
                    list_aux.append((1, 0))
                    continue
                list_aux.append((0, 0))
            list_goal.append(tuple(list_aux))
            list_aux = []
        return tuple(list_goal)

    def goal_test(self, state):
        return state in self.goal
