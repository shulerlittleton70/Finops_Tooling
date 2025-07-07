from finops_agents.agents.llm_agent import generate_sql_from_prompt, interpret_results
from finops_agents.utils.athena_utils import run_query

def main():
    question = input("💬 What question do you have about your cloud spend?\n> ")
    sql = generate_sql_from_prompt(question)
    print(f"\n🔎 Generated SQL:\n{sql}\n")

    try:
        df = run_query(sql)
        print("\n📊 Top 10 Results:\n", df.head(10))
        interpretation = interpret_results(question, df)
        print("\n💡 LLM Analysis:\n", interpretation)

        while True:
            follow_up = input("\n🔁 Ask a follow-up question (or press Enter to quit):\n> ")
            if not follow_up.strip():
                break
            sql = generate_sql_from_prompt(follow_up)
            df = run_query(sql)
            print("\n📊 Top 10 Results:\n", df.head(10))
            interpretation = interpret_results(follow_up, df)
            print("\n💡 LLM Analysis:\n", interpretation)

    except Exception as e:
        print("❌ Error running query:", e)

if __name__ == "__main__":
    main()
