import os
import openai
from finops_agents.prompt_templates import SQL_PROMPT_TEMPLATE, RESULT_INTERPRET_TEMPLATE
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a FinOps and AWS CUR expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )
    return response['choices'][0]['message']['content'].strip()

def generate_sql_from_prompt(prompt: str) -> str:
    full_prompt = SQL_PROMPT_TEMPLATE.format(question=prompt)
    return call_llm(full_prompt)

def interpret_results(question: str, dataframe: pd.DataFrame) -> str:
    preview = dataframe.head(10).to_markdown(index=False)
    full_prompt = RESULT_INTERPRET_TEMPLATE.format(
        question=question,
        dataframe_preview=preview
    )
    return call_llm(full_prompt)
