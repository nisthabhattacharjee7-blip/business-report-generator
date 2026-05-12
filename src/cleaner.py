import pandas as pd


def clean_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert columns to numeric
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Remove missing values
    df = df.dropna()

    # Remove negative quantities
    df = df[df["quantity"] >= 0]

    return df
