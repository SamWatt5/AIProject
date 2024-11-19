import pandas as pd
import numpy as np


class MovieGraph:

    def __init__(self, df):
        self.df = df
        self.numMovies = len(df)
        self.movieTitles = np.array(
            [self.df.loc[movie, "Title"] for movie in self.df.index])

        try:
            self.adjMatrix = []
            with open("adj_matrix.txt", "r") as f:
                for line in f:
                    row = list(map(float, line.strip().split(" ")))
                    self.adjMatrix.append(row)
            self.adjMatrix = np.array(self.adjMatrix)
        except FileNotFoundError:
            self.adjMatrix = self.create_adj_matrix()
            self.save_adj_matrix_to_file()

        print(f"Number of movies: {self.numMovies}")

        print("IM HERE")

    def create_adj_matrix(self):
        # creating numpy array of zeros
        # numpy arrays speedier than python list, since written in C
        adj_matrix = np.zeros((self.numMovies, self.numMovies))

        # what this is doing is getting all the criterias values from the df
        # and if it's a list, like the cast, genres etc. then it converts it to a set
        genres = self.df["Genre"].apply(set).values
        # director is a set since movies can have more than one i.e. coen brothers :)
        directors = self.df["Director"].apply(set).values
        cast = self.df["Cast"].apply(set).values
        ratings = self.df["Rating"].values

        # what these are doing is going through all the pairs of criterias, and checking similarities and adding that to a new 2d nunmpy array
        self.genre_costs = np.array([[self.genre_path_cost(genres[i], genres[j]) for j in range(
            self.numMovies)] for i in range(self.numMovies)])
        print("genres done")

        self.director_costs = np.array([[self.director_path_cost(
            directors[i], directors[j]) for j in range(self.numMovies)] for i in range(self.numMovies)])
        print("director done")

        self.cast_costs = np.array([[self.cast_path_cost(cast[i], cast[j]) for j in range(
            self.numMovies)] for i in range(self.numMovies)])
        print("cast done")

        self.rating_costs = np.array([[self.rating_path_cost(ratings[i], ratings[j]) for j in range(
            self.numMovies)] for i in range(self.numMovies)])
        print("ratings done")

        # calculates total costs
        #  - MAY CHANGE THIS TO NOT USE TOTAL AND STORE ARRAY AT EACH NODE INSTEAD
        total_costs = self.genre_costs + self.director_costs + \
            self.cast_costs + self.rating_costs

        # THIS BIT ISNT WORKING RIGHT
        # if costs are the max for all criteria, don't count, and instead just use zero
        max_genre_cost = 5
        max_director_cost = 3
        max_cast_cost = 5
        max_rating_cost = 4

        max_total_cost = max_genre_cost + \
            max_director_cost + max_cast_cost + max_rating_cost

        total_costs[total_costs >= max_total_cost] = 0

        adj_matrix = total_costs
        # MAYBE STORE THIS ALL TO A FILE SO DOESNT NEED TO RUN EVERY TIME!

        # OLD SLOW CODE (TAKES LIKE 30 MINS TO COMPLETE! :0 ):
        #
        # for i in range(self.numMovies):
        #     movie1 = self.df.iloc[i]
        #     for j in range(i + 1, self.numMovies):
        #         movie2 = self.df.iloc[j]
        #         cost = self.total_path_cost(movie1, movie2)
        #         if cost == 1:
        #             adj_matrix[i][j] = cost
        #             adj_matrix[j][i] = cost
        #             print(f"{self.movieTitles[j]} added to {
        #                   self.movieTitles[i]} because of {movie1['Director']}")
        #         print(f"{i} {j}")

        print("Created adjacency matrix!\n\n")
        return adj_matrix

    def save_adj_matrix_to_file(self):
        try:
            with open("adj_matrix.txt", 'w') as f:
                for i in range(self.numMovies):
                    row = ' '.join(map(str, self.adjMatrix[i]))
                    f.write(row + '\n')
            f.close()
        except FileNotFoundError:
            f = open("adj_matrix.txt", "x")
            f.close()
            self.save_adj_matrix_to_file()

    def get_node(self, title):
        return np.where(self.movieTitles == title)[0]

    def get_p_cost(self, movie1_title, movie2_title):
        n1 = self.get_node(movie1_title)
        n2 = self.get_node(movie2_title)
        print(f"genre: {self.genre_costs[n1, n2]}")
        print(f"director: {self.director_costs[n1, n2]}")
        print(f"cast: {self.cast_costs[n1, n2]}")
        print(f"rating: {self.rating_costs[n1, n2]}")
        return self.adjMatrix[n1, n2]

    def genre_path_cost(self, genres1, genres2):
        if genres1 == genres2:
            return 1
        elif genres1.intersection(genres2) != False:
            return 3
        else:
            return 5

    def director_path_cost(self, directors1, directors2):
        if directors1 & directors2:
            return 1
        return 3

    def cast_path_cost(self, cast1, cast2):
        if cast1 == cast2:
            return 1
        elif cast1 & cast2:
            return 3
        return 5

    def rating_path_cost(self, rating1, rating2):
        rating_diff = abs(rating1 - rating2)
        if rating_diff <= 1:
            return 1
        elif rating_diff <= 2:
            return 2
        return 4
