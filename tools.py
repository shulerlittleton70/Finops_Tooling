from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from dotenv import load_dotenv

load_dotenv()

search = SerpAPIWrapper()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Search the web using SerpAPI (Google Results)"
)

# Wikipedia tool (corrected)
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = Tool(
    name="Wikipedia",
    func=wiki_wrapper.run,
    description="Search for factual information from Wikipedia",
)
