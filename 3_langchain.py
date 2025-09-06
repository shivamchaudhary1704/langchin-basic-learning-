from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    api_key=gemini_api_key,
    temperature=0.7
)

history = []

history.append(SystemMessage(content="You are a social media expert and answer accordingly."))

print("Chatbot started. Type 'exit()' to end the conversation.")

while True:
    query = input("YOU: ")
    if query == "exit()":
        break

    history.append(HumanMessage(content=query))

    response = llm.invoke(history)
    history.append(AIMessage(content=response.content))
    
    print(f"AI: {response.content}")

print("Chat Ended")