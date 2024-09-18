# Deep dive into NLP, LLMs and Gen AI Applications

### This repository contains all the resources required to get started and build NLP applicxations, understand LLMs, build end to end solutions using  open source LLMs and Gemini models

## Running the OLLAMA Application

--  Make sure Ollama is installed locally in the system

--  Go to the terminal and run the command "ollama"

--  To use any of the open source models, run the below command

```
ollama pull <model_name>
ollama pull llama3

```
--  cd into the Ollama-LLM/Ollama_Chat folder

--  Install the required libraries using requirements file

```
python3 -m venv ollama_chat
```
--  Activate the virtual environment using the following command in the terminal

```
source ollama_chat/bin/activate
```
--  Run the **hello.py** file to simply display "hello world" 

--  Run the **convo.py** file to chat with ollama

--  Run the **user.py** file to use prompt template based on user input


## Running the Vertex AI Application

-- Create an Agent Builder and Dialogflow application using a sample file (RAG approach)

-- 