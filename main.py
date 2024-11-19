import pandas as pd
import sys
from difflib import SequenceMatcher
from PIL import ImageTk, Image
import tkinter as tk
import urllib.request
import io

from graph import MovieGraph

sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv(
    "imdb-movies-dataset.csv", encoding="utf-8", encoding_errors="replace")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.drop(columns="Review Count", inplace=True)
removed_num = 0
removed_movies = []


def main():
    graph = MovieGraph(df)
    starting_movie = search()
    other_movie = search()

    movie1 = df[df["Title"] == starting_movie]
    directors1 = movie1["Director"].iloc[0].split(", ")
    cast1 = movie1["Cast"].iloc[0].split(", ")[:3]
    genres1 = movie1["Genre"].iloc[0].split(", ")
    rating1 = movie1["Rating"].iloc[0]

    movie2 = df[df["Title"] == other_movie]
    directors2 = movie2["Director"].iloc[0].split(", ")
    cast2 = movie2["Cast"].iloc[0].split(", ")
    genres2 = movie2["Genre"].iloc[0].split(", ")
    rating2 = movie2["Rating"].iloc[0]

    print(f"genre: {graph.genre_path_cost(set(genres1), set(genres2))}\n"
          f"director: {graph.director_path_cost(
              set(directors1), set(directors2))}\n"
          f"cast: {graph.cast_path_cost(set(cast1), set(cast2))}\n"
          f"rating: {graph.rating_path_cost(rating1, rating2)}")

    # display_movie(starting_movie)


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
