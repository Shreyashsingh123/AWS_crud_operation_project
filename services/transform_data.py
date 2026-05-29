from services.utils.s3_utils import read_csv_from_s3
import pandas as pd

class transformdata:
    def __init__(self):
        pass

    def summary_metrices(self,df):
        total_sales = df['Total_Amount'].sum()

        average_sales = df['Total_Amount'].mean()

        total_quantity = df['Quantity'].sum()

        print("\nSUMMARY METRICS\n")

        print("Total Sales:", total_sales)

        print("Average Sales:", average_sales)

        print("Total Quantity Sold:", total_quantity)

    # GROUP-WISE AGGREGATION
    def category_sales(self,df):

        category_sales = df.groupby(
            'Product_Category'
        )['Total_Amount'].sum().reset_index()

        print("\nCATEGORY WISE SALES\n")

        print(category_sales)

    # CITY-WISE SALES
    def city_sales(self,df):
        city_sales = df.groupby(
            'City'
        )['Total_Amount'].sum().reset_index()

        print("\nCITY WISE SALES\n")

        print(city_sales)

    # DATE-BASED ANALYSIS
    def monthly_sales(self,df):
        monthly_sales = df.groupby(
            df['Order_Date'].dt.month
        )['Total_Amount'].sum().reset_index()

        print("\nMONTHLY SALES\n")

        print(monthly_sales)