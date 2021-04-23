# Data Mining Project 2: Filter
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal
import pandas as pd

def filter(original, genes):
    indexes = list()
    for g in genes:
        i = original[original['Gene']==g].index.values
        if i.size > 0:
            indexes.extend(i)
    df = pd.DataFrame()
    for i in indexes:
        temp = original.iloc[[i], : ]
        df = df.append(temp, ignore_index=True)

    return df

if __name__ == "__main__":
    # Get the Original data
    original = pd.read_excel("Longotor1delta.xls")
    # Get the known and the canidates
    genes = open("genes.txt").read().splitlines()
    # Go through and get only the genes we want to look at
    filtered = filter(original,genes)
    # output to excel to be normalized
    filtered.to_excel("filtered_data.xls")