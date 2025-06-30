from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel
from tools import search_tool
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor


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
            "system",
            """
            You are a research assistant that will help generate a research paper. 
            Answer the user query and use necessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools =[search_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools = tools, verbose = True) #verbose True gives me the agent thought process

query = input("What can I help you research? ")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e, "Raw Response -", raw_response)



