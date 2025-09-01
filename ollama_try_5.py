import sys
import time
from langchain_community.llms import Ollama

MODEL = "llama3"  
TEMPERATURE = 0.2

llm = Ollama(model=MODEL, temperature=TEMPERATURE)

def mk_prompt(topic):
    return f"""
Write a plain text research style report about: "{topic}".

Rules:
- No headings or bullet points.
- Just one continuous essay in natural paragraphs.
- Be clear and educational.
- Make it as detailed as you can.
"""

def ask_model(txt):
    try:
        return llm.invoke(txt)
    except Exception as e:
        print("oops model error:", e)
        return ""

def main():
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = ("weather in mumbai")
        print("ok generating…")
    time.sleep(0.5)

    prompt = mk_prompt(topic)
    txt = ask_model(prompt)

    print("\n" + "=" * 80 + "\n")
    print(txt.strip())
    print("\n" + "=" * 80 + "\n")
    print("(done!)")

main()
