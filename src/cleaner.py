import pandas as pd

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()
    
    # remove rows with missing values
    df = df.dropna()

    # covert quantity to numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

    # remove invalid quantity values
    df = df[df['quantity'] >= 0]

    return df

