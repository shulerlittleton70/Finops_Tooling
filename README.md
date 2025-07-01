# 🧠 AI Agent Integrations

A modular Python framework designed to build and orchestrate LangChain-powered agents for solving targeted business use cases in FinOps, customer success, and general research. This repository serves as a central hub for reusable tools, agent templates, and API integrations.

---

## 📌 Design Intent

This project is designed to:

- Centralize reusable AI tools for multiple business verticals (FinOps, Gainsight/CSM, Research)
- Standardize agent architecture using LangChain and Anthropic/OpenAI models
- Support flexible tool invocation via tool-calling agents
- Easily integrate with external data sources (e.g., DuckDuckGo, Wikipedia, Gainsight API, Cloud data)

---

## 📁 Directory Structure

The repository is organized into well-scoped modules and packages, each responsible for a specific domain of functionality.

```text
ai_agent_intigrations-main/
│
├── main.py                          # Entry point (can be CLI interface)
├── requirements.txt                 # Package dependencies
├── README.md                        # You are here
│
├── research_agent_general/
│   ├── __init__.py
│   └── research_agent_general.py    # Claude-based tool-calling agent for research queries
│
├── finops_agents/
│   └── __init__.py                  # Placeholder for FinOps-specific agents
│
├── customer_health_agent/
│   └── __init__.py                  # Placeholder for Gainsight-style health scoring agents
│
├── tools/
│   ├── __init__.py
│   ├── search_tools.py              # DuckDuckGo & Google search wrappers
│   ├── save_tools.py                # File saving utilities
│   ├── cloud_connection_tools.py    # Placeholder for AWS/Azure/GCP hooks
│   └── gainsight_connection.py      # Placeholder for Gainsight API integration
```

---

## 🧠 Classes & Core Objects

### `ResearchResponse` (from `research_agent_general.py`)

This Pydantic model defines the structure and format of responses returned by the research agent.

```python
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: List[str]
    tools_used: List[str]
```

This schema ensures that every agent response includes a clear topic, a detailed summary, a list of sources consulted, and a record of which tools were used to answer the query.

---

## 🔧 Key Functions & Features

### `research_agent_general.py`

This is the core agent logic for research tasks. It includes:

- **LLM Initialization**
  - Uses Anthropic’s Claude (`ChatAnthropic`) as the backend.
- **Prompt Template**
  - Uses LangChain’s `ChatPromptTemplate` to create structured, system-guided responses.
- **Tool-Calling Agent**
  - Built using `create_tool_calling_agent` and `AgentExecutor`.

#### Example Initialization

```python
agent = create_tool_calling_agent(llm, prompt, tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

#### Registered Tools

- `search_tool`: Searches the web using DuckDuckGo
- `wiki_tool`: Pulls content from Wikipedia
- `save_tool`: Persists outputs to file or storage

---

## 📦 Requirements & Installation

### Installation Steps

Install all dependencies:

```bash
pip install -r requirements.txt
```

### Declared Dependencies

The following libraries are listed in `requirements.txt`:

- `langchain`
- `langchain-community`
- `langchain-openai`
- `langchain-anthropic`
- `python-dotenv`
- `pydantic`
- `duckduckgo-search`
- `google-search-results`
- `wikipedia`

> **Note**: You may also need to manually install:
> - `anthropic` (for Claude integration)
> - `openai` (if using OpenAI models instead)

---

## 🚀 Usage Example

You can run the agent using a script or from the command line:

### CLI Usage

```bash
python main.py
```

### Programmatic Usage

```python
from research_agent_general.research_agent_general import agent_executor

response = agent_executor.invoke({"query": "What is FinOps?"})
print(response)
```

---

## 🧪 Testing

To ensure the integrity of the tools and agents:

- Use `pytest` for writing unit tests
- Mock all external API calls (search, Claude, Wikipedia)
- Validate all responses against the `ResearchResponse` schema

---

## 🧱 Extending the Project

### Adding New Tools

To create a new tool:

```python
from langchain_core.tools import tool

@tool
def my_custom_tool(input: str) -> str:
    return f"Processed: {input}"
```

Then add it to your agent:

```python
tools = [search_tool, wiki_tool, my_custom_tool]
```

This allows new integrations to be plugged in with minimal changes to the agent executor.

---

## 🤝 Contribution Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) for all naming conventions
- Use `snake_case` for file and function names
- Include documentation for new tools or modules
- Cover new features with unit tests before submitting PRs

---

## 🧬 License

This project is licensed under the MIT License.
****