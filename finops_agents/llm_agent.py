# finops_agents/llm_agent.py

from finops_agents.prompt_templates import SQL_PROMPT_TEMPLATE

# TODO: Replace this mock with actual Pedantic AI or OpenAI integration
def get_sql_from_prompt(prompt: str) -> str:
    """
    Converts a natural language question into an Athena SQL query using an LLM.
    """
    full_prompt = SQL_PROMPT_TEMPLATE.format(question=prompt)
    print("Sending prompt to LLM...")

    # Mocked SQL for now
    return f"SELECT product_code, SUM(blended_cost) AS total_cost FROM aws_cur_table GROUP BY product_code;"
