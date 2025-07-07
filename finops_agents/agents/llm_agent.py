import os
import openai
import pandas as pd
from dotenv import load_dotenv
from finops_agents.prompt_templates import SQL_PROMPT_TEMPLATE, RESULT_INTERPRET_TEMPLATE
from finops_agents.utils.cur_utils import get_cur_schema
from finops_agents.cur_dictionary import get_field_dictionary_text

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
    schema_dict = get_cur_schema()
    schema_str = "\n".join(f"- `{k}`: {v}" for k, v in schema_dict.items())
    field_docs = get_field_dictionary_text()

    full_prompt = (
        f"### CUR Table Schema:\n{schema_str}\n\n"
        f"### CUR Field Definitions:\n{field_docs}\n\n"
        + SQL_PROMPT_TEMPLATE.format(question=prompt)
    )
    return call_llm(full_prompt)

def interpret_results(question: str, dataframe: pd.DataFrame) -> str:
    preview = dataframe.head(10).to_markdown(index=False)
    field_docs = get_field_dictionary_text()
    full_prompt = RESULT_INTERPRET_TEMPLATE.format(
        question=question,
        dataframe_preview=preview
    ) + f"\n\n### CUR Field Definitions:\n{field_docs}"
    return call_llm(full_prompt)
