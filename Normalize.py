# Data Mining Project 2: Normalization
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal

import pandas as pd

def normal(df):
    # Find the Min and Max's of the three columns
    col1Min = df['sch9/wt'].min()
    col2Min = df['ras2/wt'].min()
    col3Min = df['tor1/wt'].min()

    col1Max = df['sch9/wt'].max()
    col2Max = df['ras2/wt'].max()
    col3Max = df['tor1/wt'].max()

    # Reclaculate the columns
    df['sch9/wt'] = df['sch9/wt'].apply(calc, args=(col1Min, col1Max)) # Column 1
    df['ras2/wt'] = df['ras2/wt'].apply(calc, args=(col2Min, col2Max))  # Column 2
    df['tor1/wt'] = df['tor1/wt'].apply(calc, args=(col3Min, col3Max))  # Column 3

    return df;


def calc(colVal, min, max):
    return (((colVal-min)/(max-min))*(1.0-0)+0)


if __name__ == "__main__":
    # Load the dataset
    dataset = pd.read_excel("Longotor1delta.xls")

    new_df = normal(dataset);
    new_df.to_excel("output.xls")