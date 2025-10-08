# Import required libraries
import os
from kaggle.api.kaggle_api_extended import KaggleApi
from google.cloud import storage

# Authenticate Kaggle API
api = KaggleApi()
api.authenticate()

# Define dataset details
DATASET = 'faresashraf1001/supermarket-sales'
LOCAL_FILE = 'supermarket_sales.csv'

# Download dataset from Kaggle
api.dataset_download_file(DATASET, file_name=LOCAL_FILE, path='.')
print(f"{LOCAL_FILE} downloaded successfully from Kaggle!")

# Upload the dataset to Google Cloud Storage
bucket_name = 'supermarket-sales-raw-data'
client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob('raw/supermarket_sales.csv')

# Upload file
blob.upload_from_filename(LOCAL_FILE)
print('File uploaded to GCS successfully!')
