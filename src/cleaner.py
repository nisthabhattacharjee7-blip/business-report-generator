import pandas as pd

def clean_data(df):

    print("Removing duplicates...")
    # Drop duplicates
    df = df.drop_duplicates()
    
    print("Removing rows with missing values...")
    # remove rows with missing values
    df = df.dropna()

    print("Converting quantity to numeric...")
    # covert quantity to numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

    print("Removing invalid quantity values...")
    # remove invalid quantity values
    df = df[df['quantity'] >= 0]

    return df

