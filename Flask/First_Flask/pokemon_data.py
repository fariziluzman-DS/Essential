import pandas as pd

def data_pokemon():
    df = pd.read_csv('Pokemon.csv')

    df['Type 2'].fillna('Not Yet' , inplace=True)
    return df