from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv() #loads variables such as api keys from the .env text file.

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: List[str]
    tools_used: list[str]

#establish potential llms and their model version.

#llm = ChatOpenAI(model = "gpt-4o-mini")
llm = ChatAnthropic(model = "claude-sonnet-4-20250514")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", #this is the agent prompt
            """
            Your are a research assistant that will help generate a research paper. 
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(fromat_instrucitons=parser.fet_format_instructions())









