import pandas as pd
import numpy as np

# Class for the movie graph


class MovieGraph:
    # Constructor
    def __init__(self, df):
        self.df = df
        self.numMovies = len(df)
        self.movieTitles = np.array(
            [self.df.loc[movie, "Title"] for movie in self.df.index])

        # Tries to load from file adj_matrix.txt, if not found, creates a new one
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

    # Creates an adjancency matrix from a data set
    def create_adj_matrix(self):
        # creating numpy array of zeros
        # numpy arrays speedier than python list, since written in C
        adj_matrix = np.zeros((self.numMovies, self.numMovies))

        # what this is doing is getting all the criterias values from the df
        # and if it's a list, like the cast, genres etc. then it converts it to a set
        genres = self.df["Genre"].apply(lambda x: set(x.split(", "))).values
        # director is a set since movies can have more than one i.e. coen brothers :)
        directors = self.df["Director"].apply(
            lambda x: set(x.split(", "))).values
        cast = self.df["Cast"].apply(lambda x: set(x.split(", "))).values
        ratings = self.df["Rating"].values

        # what these are doing is going through all the pairs of criterias, and checking similarities and adding that to a new 2d nunmpy array
        self.genre_costs = np.array([[self.genre_path_cost(genres[i], genres[j]) for j in range(
            self.numMovies)] for i in range(self.numMovies)])
        print("genres done")
        # self.save_intermediary_to_file("genres.txt", self.genre_costs)

        self.director_costs = np.array([[self.director_path_cost(
            directors[i], directors[j]) for j in range(self.numMovies)] for i in range(self.numMovies)])
        print("director done")
        # self.save_intermediary_to_file("directors.txt", self.director_costs)

        self.cast_costs = np.array([[self.cast_path_cost(cast[i], cast[j]) for j in range(
            self.numMovies)] for i in range(self.numMovies)])
        print("cast done")
        # self.save_intermediary_to_file("cast.txt", self.cast_costs)

        print("ratings done")
        # self.save_intermediary_to_file("ratings.txt", self.rating_costs)

        # calculates total costs
        total_costs = self.genre_costs + self.director_costs + \
            self.cast_costs
        # if costs are the max for all criteria, don't count, and instead just use zero
        max_genre_cost = 5
        max_director_cost = 3
        max_cast_cost = 5
        # max_rating_cost = 4

        max_total_cost = max_genre_cost + \
            max_director_cost + max_cast_cost

        total_costs[total_costs >= max_total_cost] = 0

        adj_matrix = total_costs

        print(f"{self.movieTitles[0]} {
              self.movieTitles[1]} {self.genre_costs[0][1]}  {self.director_costs[0][1]}  {self.cast_costs[0][1]} {adj_matrix[0][1]}")

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

    # Saves the adjancency matrix to a file
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

    def save_intermediary_to_file(self, filename, costs):
        try:
            with open(filename, 'w') as f:
                for i in range(self.numMovies):
                    row = ' '.join(map(str, costs[i]))
                    f.write(row + '\n')
            f.close()
        except FileNotFoundError:
            f = open(filename, "x")
            f.close()
            self.save_intermediary_to_file(filename)

    # Returns a node
    def get_node(self, title):
        return np.where(self.movieTitles == title)[0]

    # Returns the path cost
    def get_p_cost(self, movie1_title, movie2_title):
        n1 = self.get_node(movie1_title)
        n2 = self.get_node(movie2_title)
        print(f"genre: {self.genre_costs[n1, n2]}")
        print(f"director: {self.director_costs[n1, n2]}")
        print(f"cast: {self.cast_costs[n1, n2]}")
        print(f"rating: {self.rating_costs[n1, n2]}")
        return self.adjMatrix[n1, n2]

    # Returns the genre path cost between two movies
    def genre_path_cost(self, genres1, genres2):
        # print(f"Comparing genres: {genres1} and {genres2}")
        if genres1 == genres2:
            return 1
        elif genres1 & genres2:
            return 3
        else:
            return 5

    # Returns the director path cost between two movies
    def director_path_cost(self, directors1, directors2):
        # print(f"Comparing directors: {directors1} and {directors2}")
        if directors1 & directors2:
            return 1
        return 3

    # Returns the cast path cost between two movies
    def cast_path_cost(self, cast1, cast2):
        # print(f"Comparing cast: {cast1} and {cast2}")
        if cast1 == cast2:
            return 1
        elif cast1 & cast2:
            return 3
        return 5

    # Returns the rating path cost between two movies
    def rating_path_cost(self, rating1, rating2):
        # print(f"Comparing ratings: {rating1} and {rating2}")
        rating_diff = abs(rating1 - rating2)
        if rating_diff <= 1:
            return 1
        elif rating_diff <= 2:
            return 2
        return 4
