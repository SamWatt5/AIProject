import pandas as pd
import numpy as np


class MovieGraph:

    def __init__(self, df):
        self.df = df
        self.numMovies = len(df)
        self.movieTitles = []
        for movie in self.df.index:
            self.movieTitles.append(self.df.loc[movie, "Title"])

        self.adjMatrix = self.create_adj_matrix()

        print(f"Number of movies: {self.numMovies}")

        print(" IM HERE ")

    def create_adj_matrix(self):
        adj_matrix = np.zeros((self.numMovies, self.numMovies))

        genres = self.df["Genre"].apply(set).values
        directors = self.df["Director"].apply(set).values
        cast = self.df["Cast"].apply(set).values
        ratings = self.df["Rating"].values

        genre_costs = np.array([[self.genre_path_cost(genres[i], genres[j]) for j in range(
            self.numMovies)] for i in range(self.numMovies)])

        print("genres done")

        director_costs = np.array([[self.director_path_cost(
            directors[i], directors[j]) for j in range(self.numMovies)] for i in range(self.numMovies)])

        print("director done")

        cast_costs = np.array([[self.cast_path_cost(cast[i], cast[j]) for j in range(
            self.numMovies)] for i in range(self.numMovies)])

        print("cast done")

        rating_costs = np.array([[self.rating_path_cost(ratings[i], ratings[j]) for j in range(
            self.numMovies)] for i in range(self.numMovies)])

        print("ratings done")

        total_costs = genre_costs + director_costs + cast_costs + rating_costs

        max_genre_cost = 5
        max_director_cost = 5
        max_cast_cost = 5
        max_rating_cost = 4

        max_total_cost = max_genre_cost + \
            max_director_cost + max_cast_cost + max_rating_cost

        total_costs[total_costs == max_total_cost] == 0

        adj_matrix = total_costs

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

        return adj_matrix

    def genre_path_cost(self, genres1, genres2):
        if genres1 == genres2:
            return 1
        elif genres1 & genres2:
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
        elif cast1 & cast2:  # Check for any overlap
            return 3
        return 5

    def rating_path_cost(self, rating1, rating2):
        rating_diff = abs(rating1 - rating2)
        if rating_diff <= 1:
            return 1
        elif rating_diff <= 2:
            return 2
        return 4
