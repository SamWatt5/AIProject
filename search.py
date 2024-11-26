import numpy as np
from dataclasses import dataclass


class Problem:
    def __init__(self, startingMovie, graph, closeness):
        self.startingMovie = startingMovie
        self.graph = graph
        self.closeness = closeness

    def actions(self, movie):
        index = np.where(self.graph.movieTitles == movie)[0][0]
        print(index)
        actions_list = []
        count = 0
        for i in range(self.graph.numMovies):
            if self.graph.adjMatrix[index][i] != 0 and self.graph.adjMatrix[index][i] < self.closeness:
                actions_list.append(i)
                count += 1

        print(count)
        return actions_list

    def a_star(self, startingMovie):
        results_list = []
        currMovie = startingMovie
        table = [Table_entry(False, 0, 0) for _ in range(self.graph.numMovies)]
        while len(results_list) < 10:
            actions = actions(currMovie)
            for action in actions:
                cost = self.graph.adjMatrix[currMovie][action]
                if cost == 3:
                    results_list.append(self.result(action))
                    currMovie = action
                elif cost == 5:
                    results_list.append(self.result(action))
                    currMovie = action

    def depthSearch(self, startingMovie):
        #declare variables 
        index = np.where(self.graph.movieTitles == startingMovie)[0][0]
        stack = []
        visited = []
        allVisited = False
        top = -1
        i = 0
        order = 0
        superReleventMovies = []
        releventMovies = []

        #set the first/current movie to already being visited
        visited[index] = True

        while(allVisited == False or len(releventMovies) < 10):

            for i in range(self.graph.numMovies):
                if self.graph.adjMatrix[index][i] > 0 and visited[i] == False:
                    #add to top of stack to allow backtracking
                    top += 1
                    stack[top] = index

                    #change current index to the new indexed one
                    index = i

                    #update the current index node and say its been visited
                    visited[index] = True

                    #if the movie is closesly related add it to a list 
                    if self.graph.adjMatrix[index][i] == 3:
                        superReleventMovies.append(self.graph.movieTitles[index])
                    elif self.graph.adjMatrix[index][i] == 5:
                        releventMovies.append(self.graph.movieTitles[index])

            if top >= 0:
                index = stack[top]
                top -= 1
            else:
                allVisited = True
        
        return releventMovies
    
    def result(self, action):
        # do action on state and return new state, action is in actions_list in actions function
        # action is index in adjmatrix
        new_movie = self.graph.movieTitles[action]
        return new_movie

    def goal_test(self, movie):
        return state == self.goalState

    def path_cost(self, cost, state1, action, state2):
        # return cost of a solution path that arrives at state2 from state1 via action, default cost = 1,
        return cost+1


@dataclass
class Table_entry:
    visited: bool
    pathCost: int
    predecessor: int


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(
            self.path_cost, self.state, action, next_state))
        return next_node

    def expand(self, problem, action):
        # get list of all possible states from this state
        children = []
        for action in problem.actions(self.state):
            children.append(self.child_node(problem, action))
        return children

    def path(self):
        # find a path of nodes to this node
        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        return list(reversed(path))

    def solution(self):
        # return every action in the path
        actions = []
        for node in self.path()[1:]:
            actions.append(node.action)
        return actions


class Frontier:
    def __init__(self):
        pass
