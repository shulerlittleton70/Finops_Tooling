import os
import boto3
import pandas as pd
from pyathena import connect
import yaml
import warnings

# Load config from ../config.yaml relative to this file's directory
config_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "config.yaml")
)

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

# Extract values from config
ATHENA_DATABASE = config["athena_database"]
CUR_TABLE_NAME = config["cur_table_name"]
OUTPUT_S3_LOCATION = config["output_s3_location"]
AWS_REGION = config["aws_region"]

def run_athena_query(query: str) -> pd.DataFrame:
    """
    Execute an Athena query and return results as a DataFrame.
    Automatically replaces placeholders with config values.
    """
    warnings.filterwarnings("ignore", category=UserWarning, module="pandas")

    # Replace table placeholders with actual CUR table path
    query = query.replace("your_cur_table_name", f"{ATHENA_DATABASE}.{CUR_TABLE_NAME}")
    query = query.replace("<your_cur_table>", f"{ATHENA_DATABASE}.{CUR_TABLE_NAME}")

    try:
        print("\u25B6\uFE0F Executing SQL against Athena:")
        print(query)
        conn = connect(
            s3_staging_dir=OUTPUT_S3_LOCATION,
            region_name=AWS_REGION
        )
        df = pd.read_sql(query, conn)
        print("\u2705 Query completed.")
        return df
    except Exception as e:
        print("\u274C Error running query:", e)
        return pd.DataFrame()

def get_cur_table_columns() -> list:
    """
    Retrieve the list of columns from the CUR table using AWS Glue.
    """
    glue = boto3.client("glue", region_name=AWS_REGION)
    try:
        response = glue.get_table(
            DatabaseName=ATHENA_DATABASE,
            Name=CUR_TABLE_NAME
        )
        columns = response["Table"]["StorageDescriptor"]["Columns"]
        column_names = [col["Name"] for col in columns]
        return column_names
    except Exception as e:
        print("\u274C Failed to retrieve CUR schema from Glue:", e)
        return []