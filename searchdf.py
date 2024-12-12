import pandas as pd
import sys
from difflib import SequenceMatcher

sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv(
    "imdb-movies-dataset.csv", encoding="utf-8", encoding_errors="replace")


df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.drop(columns="Review Count", inplace=True)
removed_num = 0
removed_movies = []


def search(search_term):
    movies_found = []
    while len(movies_found) < 1:
        count = 0

        for movie in df.index:
            movie_title = df.loc[movie, "Title"]
            if (SequenceMatcher(None, search_term.capitalize(), movie_title.capitalize(), autojunk=False).ratio() > 0.75) or search_term.capitalize() in movie_title.capitalize():
                count += 1
                movies_found.append(movie_title)

        movies_found.sort()
        return movies_found
