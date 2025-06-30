from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun #QuerryRuns
from langchain_community.utilities import WikipediaAPIWrapper #APIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Search the web for information",
)