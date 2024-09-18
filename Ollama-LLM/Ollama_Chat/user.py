from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.
Here is the conversation history : {context}
Question: {question}
Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# result = chain.invoke({"context":"", "question": "What is your name ?"})
result = chain.invoke({"context":"", "question": "What is your name ?"})
print(result)

