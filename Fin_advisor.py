from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.websearch import WebSearchTools
import os
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

Fin_agent = Agent(
    name="Finance Agent",
    model=Groq(id="qwen/qwen3.6-27b"),
    role="Professional stock and financial analyst",
    instructions=[
        "Analyze stock financial data and analyst recommendations.",
        "Return concise results.",
        "Use a table for comparisons."
    ],
    tools=[YFinanceTools(
        enable_analyst_recommendations=True,
        enable_stock_price=True, 
    )],
    markdown=True,
)

web_researcher = Agent(
    # api_key = GROQ_API_KEY,
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="qwen/qwen3.6-27b"),
    tools=[WebSearchTools(
        enable_search=True,
        enable_news=True
    )],
    markdown=True,
    instructions=[
        "Find recent news about the companies being compared.",
        "Return concise results with sources."
    ]
)

Fin_team = Team(
    name="Fin Advisor Team",
    members=[Fin_agent,web_researcher],
    model=Groq(id="qwen/qwen3.6-27b"),
    instructions=[
        "Combine financial data and recent news.",
        "Compare the stocks in a concise table.",
        "Give a clear conclusion with key reasons and sources."
    ]   
)

# Fin_team.print_response(
#     "Compare NVIDIA and AMD stocks. "
#     "Give reasons behind the decision using financial data and recent news. "
#     "Show the comparison in a table."
# ) 