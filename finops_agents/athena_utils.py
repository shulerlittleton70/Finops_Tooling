# finops_agents/athena_utils.py

import pandas as pd
from pyathena import connect
import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

def get_athena_connection():
    return connect(region_name=config["aws_region"])

def run_query(query: str) -> pd.DataFrame:
    """
    Executes a SQL query against Athena and returns results as a DataFrame.
    """
    conn = get_athena_connection()
    return pd.read_sql(query, conn)
