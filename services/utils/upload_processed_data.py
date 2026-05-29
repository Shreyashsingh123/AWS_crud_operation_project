from services.utils.s3_utils import read_csv_from_s3
import pandas as pd
import boto3
from io import StringIO
from dotenv import load_dotenv
import os
load_dotenv()

df = read_csv_from_s3()

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

category_sales = df.groupby(
    'Product_Category'
)['Total_Amount'].sum().reset_index()

monthly_sales = df.groupby(
    df['Order_Date'].dt.month
)['Total_Amount'].sum().reset_index()

s3 = boto3.client('s3')

bucket_name = os.getenv('bucket_name')

category_buffer = StringIO()

category_sales.to_csv(
    category_buffer,
    index=False
)

s3.put_object(
    Bucket=bucket_name,
    Key='processed/category_sales.csv',
    Body=category_buffer.getvalue()
)

# Upload Monthly Sales

monthly_buffer = StringIO()
monthly_sales.to_csv(
    monthly_buffer,
    index=False
)

s3.put_object(
    Bucket=bucket_name,
    Key='processed/monthly_sales.csv',
    Body=monthly_buffer.getvalue()
)

print("Processed files uploaded successfully!")