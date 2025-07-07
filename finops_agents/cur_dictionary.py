# finops_agents/prompt_templates.py

SQL_PROMPT_TEMPLATE = """
You are a FinOps expert.

Write an AWS Athena SQL query using the AWS CUR dataset to answer this question:

Question: {question}

Only return valid SQL. Do not include explanations or commentary.
"""
