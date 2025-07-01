import boto3
import os

# --- S3 SESSION FACTORY ---
def create_s3_client(aws_access_key, aws_secret_key, region='us-east-1'):
    return boto3.client(
        's3',
        region_name=region,
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )

# --- LIST "DIRECTORIES" AT GIVEN PREFIX ---
def list_s3_prefixes(s3_client, bucket, prefix=''):
    paginator = s3_client.get_paginator('list_objects_v2')
    operation_parameters = {'Bucket': bucket, 'Prefix': prefix, 'Delimiter': '/'}
    result = []

    for page in paginator.paginate(**operation_parameters):
        if 'CommonPrefixes' in page:
            for p in page['CommonPrefixes']:
                result.append(p['Prefix'])

    return result

# --- LIST OBJECTS UNDER A PREFIX ---
def list_s3_objects(s3_client, bucket, prefix='', keyword=None):
    paginator = s3_client.get_paginator('list_objects_v2')
    operation_parameters = {'Bucket': bucket, 'Prefix': prefix}
    result = []

    for page in paginator.paginate(**operation_parameters):
        if 'Contents' in page:
            for obj in page['Contents']:
                key = obj['Key']
                filename = os.path.basename(key)
                if filename:  # Skip "folders"
                    if keyword is None or keyword.lower() in filename.lower():
                        result.append(obj)

    return result

# --- DOWNLOAD A SPECIFIC OBJECT ---
def download_s3_object(s3_client, bucket, key, local_dir='.'):
    filename = os.path.basename(key)
    local_path = os.path.join(local_dir, filename)
    os.makedirs(local_dir, exist_ok=True)
    s3_client.download_file(bucket, key, local_path)
    return local_path
