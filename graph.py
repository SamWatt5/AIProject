import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "imdb-movies-dataset.csv", encoding="utf-8", encoding_errors="replace")

df.plot(kind='scatter', x='Rating', y='Metascore')
plt.show()

# USE ARRAY FOR EDGES
# IF NOTHING RELATED SET EDGE TO 0 ELSE USE PATH COST FUNCTION TO GET ARRAY
