from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import initialize_agent, Tool, AgentType

api_key = #write your api key here(GEMINI)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.7,
    google_api_key=api_key
)
wiki = WikipediaAPIWrapper(top_k_results=5)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki)




tools = [
    Tool(
        name="Wikipedia",
        func=wiki_tool.run,
        description="Use for background info, definitions, and summaries"
    )
]


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
def research_technology(topic: str):
    system_prompt = f"""
You are a research assistant. Write a detailed structured report about the technology: "{topic}".
Follow this structure:
- Introduction
- Background
- Current Trends
- Key Data/Stats
- Opportunities/Risks
- Conclusion
Make it concise but informative using information from Wikipedia.
Do NOT include source URLs.
"""
    report = agent.run(system_prompt)
    print(report)


if __name__ == "__main__":
    topic = input("Enter the technology to research: ")
    research_technology(topic)

