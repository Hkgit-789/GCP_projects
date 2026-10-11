from google.cloud import storage
import os
import pandas as pd
from io import BytesIO

# ----------------------------------------------------
# Create GCS Client
# ----------------------------------------------------
client = storage.Client()

# ----------------------------------------------------
# List all buckets
# ----------------------------------------------------
print("\nAvailable Buckets")
print("-" * 40)

buckets = client.list_buckets()
print(buckets)
for bucket in buckets:
    print(bucket.name)

    # ----------------------------------------------------
# Select bucket
# ----------------------------------------------------
bucket_name = "pipeline_usecase1"

bucket = client.bucket(bucket_name)
print("\nFiles inside bucket")
print("-" * 40)
print(bucket)
print(type(bucket))
# ----------------------------------------------------
# List files inside bucket
# ----------------------------------------------------
blobs=client.list_blobs("pipeline_usecase1")

for blob in blobs:
    print(blob.name)
    if (blob.name).endswith('.csv'):
        print('condition validated')
        file_data=blob.download_as_bytes()
        df=pd.read_csv(BytesIO(file_data))
        print('\nschema is')
        print(df.dtypes)
        print('\n first rows')
        print(df.head())




