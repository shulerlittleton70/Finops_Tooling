# finops_agents/utils/athena_utils.py

import pandas as pd
from pyathena import connect
import yaml
import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

def get_athena_connection():
    return connect(
        region_name=config["aws_region"],
        s3_staging_dir=config["output_s3_location"],
        schema_name=config["athena_database"]
    )

def run_query(query: str) -> pd.DataFrame:
    conn = get_athena_connection()
    return pd.read_sql(query, conn)
