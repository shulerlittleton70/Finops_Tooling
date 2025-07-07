# finops_agents/app.py

from finops_agents.agents.llm_agent import get_sql_from_prompt
from finops_agents.utils.athena_utils import run_query

def main():
    question = input("Enter your FinOps question: ")
    sql = get_sql_from_prompt(question)
    print(f"\nGenerated SQL:\n{sql}\n")

    try:
        df = run_query(sql)
        print("Top 10 Results:\n", df.head(10))
    except Exception as e:
        print("Query execution failed:", e)

if __name__ == "__main__":
    main()
