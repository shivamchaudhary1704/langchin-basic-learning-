from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",  
    api_key = gemini_api_key, 
    temperature=0.7
)

response = llm.invoke("square of 7")
print(response.content)
