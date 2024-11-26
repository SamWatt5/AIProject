import pandas as pd
import sys
from difflib import SequenceMatcher
from PIL import ImageTk, Image
import tkinter as tk
import urllib.request
import io

from search import *
from graph import MovieGraph

# Creatign the data frame
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv(
    "imdb-movies-dataset.csv", encoding="utf-8", encoding_errors="replace")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.drop(columns="Review Count", inplace=True)
removed_num = 0
removed_movies = []

# Main function


def main():
    # Creating the movie graph
    graph = MovieGraph(df)

    # Searching for movie titles
    starting_movie_title = search()
    # starting_movie = df[df["Title"] == starting_movie_title]

    # problem = Problem(starting_movie_title, graph, 10)
    # print(problem.actions(starting_movie_title))

    # results = problem.do_searches(starting_movie_title)
    results = [search() for _ in range(3)]
    display_results(starting_movie_title, results)


def display_results(startingMovie, results):
    window = tk.Tk()
    window.configure(bg="#caf0f8")
    starting_box = create_movie_box(startingMovie)
    boxes = []
    for movie in results:
        boxes.append(create_movie_box(movie))

    starting_box.grid(row=0, column=1, padx=10, pady=10)

    for i, box in enumerate(boxes):
        r = i // 3
        c = i % 3
        box.grid(row=r+1, column=c, padx=10, pady=10)

    # largestWidth = 0
    # for box in boxes:
    #     if box.winfo_width() > largestWidth:
    #         largestWidth = box.winfo_width()

    # starting_box.configure(width=largestWidth)
    # for box in boxes:
    #     box.configure(width=largestWidth)

    window.mainloop()


def create_movie_box(movie_title):
    print("\nDisplaying Movie.....\n")
    movie = df[df["Title"] == movie_title]
    director = movie["Director"].iloc[0]
    cast = movie["Cast"].iloc[0].split(", ")[:3]
    genres = movie["Genre"].iloc[0].split(", ")

    print("Title:\n  " + movie_title + "\n")
    print("Director:\n  " + director + "\n")
    print("Cast:")
    for actor in cast:
        print("  " + actor)
    print("")
    print("Genres:")
    for genre in genres:
        print("  " + genre)

    poster_url = movie["Poster"].iloc[0]
    with urllib.request.urlopen(poster_url) as u:
        raw_data = u.read()
    image = Image.open(io.BytesIO(raw_data))
    root = tk.Frame(bg="#90e0ef", width=300)
    photo = ImageTk.PhotoImage(image)
    poster_label = tk.Label(root, image=photo)
    title_label = tk.Label(root, text=movie_title,
                           font="tkHeadingFont", bg="#90e0ef")
    director_label = tk.Label(root, text=(
        "Directed by: " + director), bg="#90e0ef")
    actor_labels = [tk.Label(root, text="Cast:", bg="#90e0ef")]
    for actor in cast:
        actor_labels.append(tk.Label(root, text=(actor), bg="#90e0ef"))
    genre_labels = [tk.Label(root, text="Genres:", bg="#90e0ef")]
    for genre in genres:
        genre_labels.append(tk.Label(root, text=(genre), bg="#90e0ef"))

    poster_label.pack()
    title_label.pack()
    director_label.pack()
    for label in actor_labels:
        label.pack()
    for label in genre_labels:
        label.pack()

    return root


def display_movie(movie_title):
    print("\nDisplaying Movie.....\n")
    movie = df[df["Title"] == movie_title]
    director = movie["Director"].iloc[0]
    cast = movie["Cast"].iloc[0].split(", ")[:3]
    genres = movie["Genre"].iloc[0].split(", ")

    print("Title:\n  " + movie_title + "\n")
    print("Director:\n  " + director + "\n")
    print("Cast:")
    for actor in cast:
        print("  " + actor)
    print("")
    print("Genres:")
    for genre in genres:
        print("  " + genre)

    poster_url = movie["Poster"].iloc[0]
    with urllib.request.urlopen(poster_url) as u:
        raw_data = u.read()
    image = Image.open(io.BytesIO(raw_data))
    root = tk.Tk()
    # image = image.resize((image.width*2, image.height*2))
    photo = ImageTk.PhotoImage(image)
    poster_label = tk.Label(root, image=photo)
    title_label = tk.Label(root, text=movie_title, font="tkHeadingFont")
    director_label = tk.Label(root, text=("Directed by: " + director))
    actor_labels = [tk.Label(root, text="Cast:")]
    for actor in cast:
        actor_labels.append(tk.Label(root, text=(actor)))
    genre_labels = [tk.Label(root, text="Genres:")]
    for genre in genres:
        genre_labels.append(tk.Label(root, text=(genre)))

    poster_label.pack()
    title_label.pack()
    director_label.pack()
    for label in actor_labels:
        label.pack()
    for label in genre_labels:
        label.pack()

    root.mainloop()


def search():
    movies_found = []
    while len(movies_found) < 1:
        search_term = input("Please search for a movie: ")
        count = 0

        for movie in df.index:
            movie_title = df.loc[movie, "Title"]
            if (SequenceMatcher(None, search_term.capitalize(), movie_title.capitalize(), autojunk=False).ratio() > 0.75) or search_term.capitalize() in movie_title.capitalize():
                count += 1
                movies_found.append(movie_title)

        movies_found.sort()

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


main()
