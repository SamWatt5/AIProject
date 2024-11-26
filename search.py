import numpy as np
from dataclasses import dataclass
from collections import deque

class Node:
    pass


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

    # Uniformed search
    
    # Using bfs to find 10 movies with clossness of less than 7 and store them in an array
    def bfs(self, startingMovie):
        results = []
        queue = deque()
        visited = set()

        # Get the index of the starting movie
        try:
            startIndex = np.where(self.graph.movieTitles == startingMovie)[0][0]
        except IndexError:
            print("Starting movie not found in graph.")
            return results
        
        # Initialisng the bfs queue with the starting movie
        queue.append(startIndex)
        visited.add(startIndex)

        while queue and len(results) < 10:
            curr = queue.popleft()

            # Explore neighbors of the current movie
            for neighbor in range(self.graph.numMovies):
                closeness = self.graph.adjMatrix[curr][neighbor]
                if neighbor not in visited and closeness != 0 and closeness <self.closeness:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    results.append(self.graph.movieTitles[neighbor])

                    if len(results) == 10:
                        break
        return results

    # Informed search 
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
        return results_list

    def combine_searches(list1, list2, list3):
        combined_results = []
        for movie in list1:
            if (movie in list2) or (movie in list3):
                combined_results.append(movie)
        for movie in list2:
            if movie in list3 and movie not in combined_results:
                combined_results.append(movie)
        return combined_results

    def do_searches(self, startingMovie):
        bfs_results = self.bfs(startingMovie)
        dfs_results = self.dfs(startingMovie)
        as_results = self.a_star(startingMovie)

        combined_results = self.combine_searches(
            bfs_results, dfs_results, as_results)

        return combined_results

    def depthSearch(self, startingMovie):
        index = np.where(self.graph.movieTitles == startingMovie)[0][0]
        stack = []
        visited = []
        allVisited = False
        top = -1
        i = 0
        order = 0

        visited[index] = True

        while(allVisited == False):

            for i in range(self.graph.numMovies):
                i += 1
                if self.graph.adjMatrix

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
