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

def conversations():
    context = ""
    print("Chat Application !")
    while True:
        user_input =  input("User :")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"context":context, "question": user_input})
        print("Model : ", result)
        context+=f"\nUser: {user_input}\n Model: {result}"

if __name__ == "__main__":
    conversations()