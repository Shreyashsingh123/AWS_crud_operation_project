import boto3

# Create S3 client
s3 = boto3.client('s3')

# Bucket details
bucket_name = 'practice-project-raw'

# File in S3
s3_key = 'raw/sample.csv'

# Local download path
download_path = '../output/downloaded_sample.csv'

# Download file
s3.download_file(
    bucket_name,
    s3_key,
    download_path
)

print("File downloaded successfully!")