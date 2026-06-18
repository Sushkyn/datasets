import pandas as pd

df = pd.read_json("data/movies.json")

df = df.dropna()

df.to_csv("data/clean_movies.csv", index=False)

print("Data cleaned successfully")
