# Read file from S3 to reuse it again and again in project
import boto3
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

def read_csv_from_s3():
    s3 = boto3.client('s3')
    bucket_name = os.getenv('bucket_name')
    file_key = os.getenv('s3_key')
    obj = s3.get_object(
        Bucket=bucket_name,
        Key=file_key
    )
    df = pd.read_csv(obj['Body'])

    return df
