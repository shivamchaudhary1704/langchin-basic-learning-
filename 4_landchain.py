from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import firestore
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from dotenv import load_dotenv
import os#os need more prac

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

PROJECT_ID="try-1-185e3"
SESSION_ID="user_new_setion"
COLLECTION_NAME="chat_history"

client=firestore.Client(project=PROJECT_ID)



# Start with an empty history list
history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client
)
print("current history is")
print(history.messages)


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    api_key=gemini_api_key,
    temperature=0.7
)
# ✅ CORRECT: Append an instance of SystemMessage with its content
#history.ad(SystemMessage(content="You are a social media expert and answer accordingly."))

print("Chatbot started. Type 'exit()' to end the conversation.")

while True:
    query = input("YOU: ")
    if query == "exit()":
        break
    
    # ✅ CORRECT: Append an instance of HumanMessage with the user's query
    history.add_user_message(HumanMessage(content=query))
    
    # Invoke the model with the full history
    response = llm.invoke(history.messages)
    
    # ✅ CORRECT: Append an instance of AIMessage with the AI's response
    history.add_ai_message(AIMessage(content=response.content))
    
    # Print the AI's response
    print(f"AI: {response.content}")


print("Chat Ended")
