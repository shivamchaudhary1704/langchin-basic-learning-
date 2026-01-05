from langchain_google_genai import ChatGoogleGenerativeA
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",  
    api_key = gemini_api_key, 
    temperature=0.7
)


messages =[
    SystemMessage("you are a socialmedia exper and answer accoring"),
    HumanMessage("give a shirt tip to make my social media post engaing")
]
response = llm.invoke(messages)
print(response.content)


