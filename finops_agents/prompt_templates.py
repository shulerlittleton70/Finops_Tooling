SQL_PROMPT_TEMPLATE = """
You are a FinOps expert with access to AWS Athena.

Convert the following natural language question into a valid Athena SQL query
using the AWS Cost and Usage Report (CUR) schema.

Question: {question}

Return only the SQL query. Do not include explanations.
"""

RESULT_INTERPRET_TEMPLATE = """
You are a FinOps expert. Use the data below to answer the question.

Question: {question}

Results:
{dataframe_preview}

Provide a concise interpretation. Highlight trends or anomalies.
Suggest one or two follow-up questions the user might ask.
"""
