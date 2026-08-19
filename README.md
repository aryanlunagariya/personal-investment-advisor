# Personal Investment Advisor

An AI-powered personal investment research assistant built with
**Python, Agno, Groq, Tavily, and Yahoo Finance**. The project uses
multiple AI agents to analyze financial data, retrieve analyst
recommendations, and research the latest news about companies.

## Features

-   🤖 Multi-agent AI architecture using Agno
-   📊 Stock and financial data using YFinanceTools
-   📈 Analyst recommendations
-   🔎 Latest web/news research using Tavily
-   🧠 Groq-powered LLMs
-   🤝 Team of specialized agents:
    -   **Financial Analyst** --- retrieves stock and analyst
        information
    -   **Web Researcher** --- searches for recent company news
    -   **Team Agent** --- combines the results into a concise response
-   📝 Markdown-formatted responses and comparison tables

## Tech Stack

-   Python
-   Agno
-   Groq
-   WebSearchTools
-   yfinance
-   python-dotenv

## Project Structure

``` text
Personal Investment Advisor/
│
├── .env                  # API keys - do not upload to GitHub
├── .gitignore
├── Finance_advisor.py    # Main AI investment advisor
├── Fin_advisor.py
├── check.py              # This file is used to check the available & Accessible Model  by the API
├── ui.py                 # Interface of the Design
├── requirement.txt       
├── pyproject.toml
└── README.md
```

## Installation

### 1. Clone the repository

``` bash
git clone https://github.com/aryanlunagariya/personal-investment-advisor
cd personal-investment-advisor
```

### 2. Create and activate a virtual environment

Using Python:

``` bash
python -m venv .venv
```

Windows PowerShell:

``` powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

``` bash
pip install -r requirement.txt
```

If you use `uv`:

``` bash
uv sync
```

## Environment Variables

Create a `.env` file in the project root:

``` env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

**Never commit your `.env` file or API keys to GitHub.**

## Usage

Run the advisor with:

``` bash
python Finance_advisor.py
```

Example query:

``` text
Summarize the analyst recommendations and share the latest information about Google.
```

The system can delegate different parts of the request to specialized
agents and combine their results.

## How It Works

``` text
                    User Query
                        │
                        ▼
                 ┌──────────────┐
                 │  Team Agent  │
                 └──────┬───────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
    ┌─────────────────┐    ┌─────────────────┐
    │ Financial Agent │    │ Web Researcher  │
    ├─────────────────┤    ├─────────────────┤
    │    YFinance     │    │  WebSearchTool  │
    │ Analyst Ratings │    │   Latest News   │
    └────────┬────────┘    └────────┬────────┘
             │                      │
             └──────────┬───────────┘
                        ▼
                 Combined Analysis
                        │
                        ▼
                   Final Response
```

## Example Use Cases

-   Analyze a company's analyst recommendations
-   Research recent company news
-   Compare financial information
-   Combine market data with current news
-   Perform preliminary investment research

## Disclaimer

This project is intended for **educational and research purposes only**.
It does not provide personalized financial advice, investment
recommendations, or guaranteed market predictions.

Always verify financial information using reliable sources and consult a
qualified financial professional before making investment decisions.

## Future Improvements

-   Streamlit web interface
-   Portfolio tracking
-   Stock comparison dashboard
-   Risk analysis
-   Financial charts
-   More financial data sources
-   Persistent user preferences
-   Improved agent orchestration
-   Real-time market alerts

## Author

**Aryan Lunagariya**

Built as a Generative AI / Agentic AI project to explore multi-agent
systems, financial research, tool calling, and LLM-based applications.
