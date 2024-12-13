import numpy as np
import math
from collections import deque


# Class for defining the problem
class Problem:
    # definition of initial state
    def __init__(self, startingMovie, graph, closeness):
        self.startingMovie = startingMovie
        self.graph = graph
        self.closeness = closeness

    # definition of actions
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
            startIndex = np.where(
                self.graph.movieTitles == startingMovie)[0][0]
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
                if neighbor not in visited and closeness != 0 and closeness < self.closeness:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    results.append(self.graph.movieTitles[neighbor])

                    if len(results) == 10:
                        break
        return results

    # method to make greedy search recursive
    def greedyBestRecursive(self, curr, visited, results, isFirstMovie=False):
        if len(results) == 10:
            return
        visited.add(curr)
        if not isFirstMovie:
            results.append(self.graph.movieTitles[curr])

        closest_neighbor = None
        closest_closeness = math.inf
        for neighbor in range(self.graph.numMovies):
            closeness = self.graph.adjMatrix[curr][neighbor]
            if closeness != 0 and neighbor not in visited and closeness < closest_closeness:
                closest_closeness = closeness
                closest_neighbor = neighbor

        if closest_neighbor is not None:
            self.greedyBestRecursive(closest_neighbor, visited, results)

    # method to start greedy best first search
    def greedyBest(self, startingMovie):
        results = []
        visited = set()

        # Get the index of the starting movie
        try:
            startIndex = np.where(
                self.graph.movieTitles == startingMovie)[0][0]
        except IndexError:
            print("Starting movie not found in graph.")
            return results

        # Initialisng the dfs stack with the starting movie
        visited.add(startIndex)

        self.greedyBestRecursive(startIndex, visited, results, True)
        return results

    # method to make the dfs recursive
    def dfsRecursive(self, curr, visited, results, isFirstMovie=False):
        if len(results) == 10:
            return
        visited.add(curr)
        if not isFirstMovie:
            results.append(self.graph.movieTitles[curr])

        for neighbor in range(self.graph.numMovies):
            if self.graph.adjMatrix[curr][neighbor] != 0 and neighbor not in visited:
                self.dfsRecursive(neighbor, visited, results)

    # method for dfs
    def dfs(self, startingMovie):
        results = []
        visited = set()

        # Get the index of the starting movie
        try:
            startIndex = np.where(
                self.graph.movieTitles == startingMovie)[0][0]
        except IndexError:
            print("Starting movie not found in graph.")
            return results

        # Initialisng the dfs stack with the starting movie
        visited.add(startIndex)

        self.dfsRecursive(startIndex, visited, results, True)
        return results

    # Combines the result of all three searches
    def combine_searches(self, list1, list2, list3):
        combined_results = []
        for movie in list1:
            combined_results.append(movie)
        for movie in list2:
            if movie not in combined_results:
                combined_results.append(movie)
        for movie in list3:
            if movie not in combined_results:
                combined_results.append(movie)

        return combined_results

    # This does the searches and returns the result
    def do_searches(self, startingMovie):
        bfs_results = self.bfs(startingMovie)
        dfs_results = self.dfs(startingMovie)
        greedy_best_results = self.greedyBest(startingMovie)

        combined_results = self.combine_searches(
            bfs_results, dfs_results, greedy_best_results)
        return combined_results
