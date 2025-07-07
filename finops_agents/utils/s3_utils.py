# finops_agents/utils/s3_utils.py

import boto3

def list_cur_files(bucket_name, prefix=""):
    """
    List CUR files in the specified S3 bucket.
    """
    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    return [obj["Key"] for obj in response.get("Contents", [])]
