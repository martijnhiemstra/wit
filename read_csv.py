print("Start cvs uitlezen")

import pandas

# Wij gebruiken pandas om een cvs uit te lezen en in een dataframe te zetten
df = pandas.read_csv('pokemon.csv')

# print(df["Name"])

for r,rij in df.iterrows():
    print(rij["Name"])
