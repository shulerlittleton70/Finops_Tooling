from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

#establish potential llms and their model version. Would like to write documentation up on available models and which to select
llm2 = ChatOpenAI(model = "gpt-4o-mini")
llm = ChatAnthropic(model = "claude-sonnet-4-20250514")

response = llm.invoke("What is the meaning of life?")
print(response.content)













