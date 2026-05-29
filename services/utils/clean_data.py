import pandas as pd

def clean_data(df):
    df = df.dropna()

    df['Order_Date'] = pd.to_datetime(df['Order_Date'])

    df['Quantity'] = df['Quantity'].astype(int)

    df['Unit_Price'] = df['Unit_Price'].astype(float)

    df['Total_Amount'] = df['Total_Amount'].astype(float)

    print("\nData Cleaned Successfully!\n")
    return df