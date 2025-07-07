# finops_agents/utils/cur_utils.py

import boto3
import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

def get_cur_schema() -> dict:
    """
    Retrieves the CUR table schema (column names and types) from AWS Glue.
    Returns a dictionary of {column_name: type}.
    """
    glue = boto3.client("glue", region_name=config["aws_region"])
    response = glue.get_table(
        DatabaseName=config["athena_database"],
        Name=config["cur_table_name"]
    )
    columns = response['Table']['StorageDescriptor']['Columns']
    return {col['Name']: col['Type'] for col in columns}
