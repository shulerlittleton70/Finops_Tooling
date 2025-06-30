from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def save_to_txt(data:str, filename: str ="research_output.txt"):
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    formatted_text = f'---Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n'
    with open(filename,"a", encoding= "utf-8") as f:
        f.write(formatted_text)

    return f"Data  successfully saved to {filename}"

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
