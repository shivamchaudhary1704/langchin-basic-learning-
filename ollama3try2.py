from langchain_community.llms import Ollama

llm = Ollama(model="llama3", temperature=0.2)

topic = "weather in delhi"

prompt = f"""
Write a plain text report about: "{topic}".
No headings, no bullet points, just a continuous essay in simple paragraphs.
"""

print("ok generating...\n")

report = llm.invoke(prompt)

print("=============================================================")
print(report)
print("==============================================================")
print("done!")
