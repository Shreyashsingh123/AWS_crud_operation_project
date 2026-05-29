import boto3
from dotenv import load_dotenv
import os
load_dotenv()

s3 = boto3.client('s3')

bucket_name = os.getenv('bucket_name')
# Local file path
file_path = os.getenv('file_path')

# S3 destination path
s3_key =os.getenv('s3_key')

s3.upload_file(
    file_path,
    bucket_name,
    s3_key
)

print("File uploaded successfully!")