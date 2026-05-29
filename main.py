import boto3
import pandas as pd
from services.utils.clean_data import clean_data
from services.transform_data import transformdata
from services.utils.s3_utils import read_csv_from_s3
from services.SQL.Aggregation import salestransaction


def main():
        
    df=read_csv_from_s3()
    df1=clean_data(df)
    tr=transformdata()
    tr.summary_metrices(df1)
    tr.city_sales(df1)
    tr.monthly_sales(df1)
    tr.category_sales(df1)

    sl=salestransaction()
    sl.Aggregate_function()
    sl.date_based_filtering()
    sl.group_by_having()
    sl.sort_data()
    sl.top_bottom_performer()
    sl.connection_close()

if __name__=='__main__':
    main()

    # insert_data(df)