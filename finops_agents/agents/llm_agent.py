# finops_agents/agents/llm_agent.py

from finops_agents.prompt_templates import SQL_PROMPT_TEMPLATE

# TODO: Replace with actual call to Pedantic AI, OpenAI, or other LLM
def get_sql_from_prompt(prompt: str) -> str:
    """
    Converts a natural language FinOps prompt into an Athena SQL query using LLM.
    """
    full_prompt = SQL_PROMPT_TEMPLATE.format(question=prompt)
    print("Sending prompt to LLM...")

    # Simulated LLM output (replace with real API)
    return (
        "SELECT product_code, SUM(blended_cost) AS total_cost "
        "FROM aws_cur_table GROUP BY product_code;"
    )
