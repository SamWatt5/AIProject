import pandas as pd
import sys
from difflib import SequenceMatcher
from PIL import ImageTk, Image
import tkinter as tk
import urllib.request
import io
from flask import Flask
from flask_cors import CORS
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

# Setting up flask

app = Flask(__name__)
CORS(app)

graph = None


def createGraph():
    global graph

    graph = MovieGraph(df)
    return graph


print("Creating graph... this might take awhile")
createGraph()
print("Graph created, server is now online")


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/search/<name>')
def searchRoute(name):
    movies = search(name)
    return {
        'movies': movies
    }


@app.route('/movies')
def movies():
    return {
        'length': len(df)
    }


@app.route('/movie/<name>')
def movieInfo(name):
    problem = Problem(name, graph, 10)
    results = problem.do_searches(name)
    results = {}

    for movie_title in results:
        movie = df[df["Title"] == movie_title]
        results[movie_title] = {
            "Title": movie_title,
            "Rating": movie["Rating"].iloc[0],
            "Genre": movie["Genre"].iloc[0],
            "Director": movie["Director"].iloc[0],
            "Description": movie["Description"].iloc[0],
            "Poster": movie["Poster"].iloc[0]
        }
    return results


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
