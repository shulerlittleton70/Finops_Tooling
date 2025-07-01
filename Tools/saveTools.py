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

save_tool = Tool(
    name="save_text_tool",
    func=save_to_txt,
    description="Saves response to text file."
)