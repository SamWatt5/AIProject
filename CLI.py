import pandas as pd
import sys
from search import *
from graph import MovieGraph
from searchdf import search

# Creatign the data frame
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv(
    "imdb-movies-dataset.csv", encoding="utf-8", encoding_errors="replace")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.drop(columns="Review Count", inplace=True)
removed_num = 0
removed_movies = []


def get_movie_name():
    movie_name = input("Enter a movie name: ")
    return movie_name


def menu():
    choice = 0
    while True:
        print("\nPlease enter a new movie title or just press enter to exit the program:")
        choice = input()
        if choice:
            start(choice)
        else:
            break


def cli_search(movie_title):
    movies_found = search(movie_title)

    match len(movies_found):
        case 0:
            print("No movies found")
        case 1:
            print("One movie found!")
            return movies_found[0]
        case _:
            print("Found more than one movie, please choose(1-" +
                  str(len(movies_found)) + ")")
            i = 1
            for movie in movies_found:
                print(str(i) + ". " + movie)
                i += 1

    choice = int(input("\n"))
    return movies_found[choice-1]


def print_movie(movie_title):
    movie = df[df["Title"] == movie_title]

    print(movie_title)
    print(f"Director: {movie["Director"].iloc[0]}")
    print(f"Cast: {movie["Cast"].iloc[0]}")
    print(f"Genre: {movie["Genre"].iloc[0]}")
    print(f"Description: {movie["Description"].iloc[0]}\n")


def start(movie_title):
    starting_movie = cli_search(movie_title)
    print_movie(starting_movie)

    problem = Problem(starting_movie, graph, 10)
    search_results = problem.do_searches(starting_movie)

    for i, movie in enumerate(search_results):
        print(f"{i+1}.")
        print_movie(movie)


if __name__ == '__main__':
    print("Loading Movies... this might take awhile")
    graph = MovieGraph(df)
    print("Movies loaded!")

    starting_title = get_movie_name()
    start(starting_title)

    menu()
