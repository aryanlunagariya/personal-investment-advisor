from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    description="you are an assistant please reply based on the question",
    instructions=["Get analyst recommendations for Alphabet.",
            "Return concise results.",
            "Use a table for comparisons."],
    # tools=[DuckDuckGoTools(
    #     enable_search=True,
    #     enable_news=False,
    #     fixed_max_results=5
    # )],
    markdown=True,

)

agent.print_response("give me little bit information about Operation Sindoor")
