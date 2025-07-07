# finops_agents/utils/athena_utils.py

import pandas as pd
from pyathena import connect
import yaml
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load Athena config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

def get_athena_connection():
    """
    Establishes and returns a connection to AWS Athena using PyAthena.
    Credentials are sourced from environment variables loaded by .env.
    """
    return connect(region_name=config["aws_region"])

def run_query(query: str) -> pd.DataFrame:
    """
    Executes a SQL query against AWS Athena and returns results as a pandas DataFrame.
    """
    conn = get_athena_connection()
    return pd.read_sql(query, conn)
