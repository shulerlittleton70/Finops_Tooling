# finops_agents/prompt_templates.py

SQL_PROMPT_TEMPLATE = """
You are a FinOps expert with access to AWS Athena.

Convert the following natural language question into an Athena SQL query
that uses the CUR table. Assume the table contains fields like product_code, usage_start_date, blended_cost, etc.

Question: {question}

Only return a valid SQL query. Do not include any commentary.
"""
