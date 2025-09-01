from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from docx import Document
import os

llm = Ollama(model="llama3")

topic = "weather in delhi"

prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="""
    Generate a comprehensive report on the following topic.
    The report should be well-structured with a clear introduction,
    main body, and conclusion. Include key facts, recent developments,
    and potential future trends.

    Topic: {topic}

    ---
    Report:
    """
)
report_chain = LLMChain(llm=llm, prompt=prompt_template)

print(f"Generating report on: {topic}...\n")

response = report_chain.invoke({"topic": topic})

report_text = response["text"]

print("\n--- Generated Report ---")
print(report_text)

print("=================creating a doc file for your report====================")
doc = Document()
doc.add_paragraph(report_text)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "output.docx")
doc.save(file_path)

print(f"Word file created at: {file_path}")
