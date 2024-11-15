import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv(
    "imdb-movies-dataset.csv", encoding="utf-8", encoding_errors="replace")

df.plot(kind='scatter', x='Rating', y='Metascore')
plt.show()
