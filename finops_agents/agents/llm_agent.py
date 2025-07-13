# finops_agents/agents/llm_agent.py

import os
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sql_from_prompt(prompt: str) -> str:
    """
    Generates an SQL query from a natural language prompt using OpenAI LLM.
    """
    print(f"💡 Using LLM to generate SQL from prompt: {prompt}")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a cloud cost optimization assistant. Generate AWS CUR-compatible SQL from user questions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    sql = response.choices[0].message.content.strip()
    print("🔎 Generated SQL:\n", sql)
    return sql

def interpret_results(dataframe: pd.DataFrame, user_prompt: str) -> str:
    """
    Interpret the returned DataFrame with context to the original question.
    """
    if dataframe.empty:
        return "⚠️ No results returned."

    interpretation = f"Here is a summary of the results for your question: \n**{user_prompt}**\n\n"
    interpretation += dataframe.head(5).to_markdown(index=False)
    return interpretation
