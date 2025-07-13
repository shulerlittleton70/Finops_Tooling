# finops_agents/app.py

import os
import yaml
from finops_agents.agents.llm_agent import generate_sql_from_prompt, interpret_results
from finops_agents.utils.athena_utils import run_athena_query

# Load config.yaml relative to this file
current_dir = os.path.dirname(__file__)
config_path = os.path.abspath(os.path.join(current_dir, "config.yaml"))

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

table_name = config["cur_table_name"]

def main():
    print("💬 What question do you have about your cloud spend?")
    question = input("> ")

    sql = generate_sql_from_prompt(question)
    print("\n🔎 Generated SQL:\n", sql)

    # Inject real table name
    sql = sql.replace("your_cur_table_name", table_name)

    df = run_athena_query(sql)

    if not df.empty:
        interpretation = interpret_results(df, question)
        print("\n📊 Result Summary:\n", interpretation)
    else:
        print("⚠️ No results returned.")

if __name__ == "__main__":
    main()
