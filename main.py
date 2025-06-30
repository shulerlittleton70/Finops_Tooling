from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

#establish potential llms and their model version. Would like to write documentation up on available models and which to select
llm = ChatOpenAI(model = "gpt-4o-mini")
llm2 = ChatAnthropic(model = "claud-3-5-sonnet-20241022")













