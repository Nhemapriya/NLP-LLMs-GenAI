# Deep dive into NLP, LLMs and Gen AI Applications

### This repository contains all the resources required to get started and build NLP applications, understand LLMs, build end to end solutions using  open source LLMs and Gemini models

## Running the OLLAMA Application

-  Make sure Ollama is installed locally in the system

-  Go to the terminal and run the command "ollama"

-  To use any of the open source models, run the below command

```
ollama pull <model_name>
ollama pull llama3
```
-  cd into the Ollama-LLM/Ollama_Chat folder

-  Install the required libraries using requirements file

```
python3 -m venv ollama_chat
```
-  Activate the virtual environment using the following command in the terminal

```
source ollama_chat/bin/activate
```
-  Run the **hello.py** file to simply display "hello world" 

-  Run the **convo.py** file to chat with ollama

-  Run the **user.py** file to use prompt template based on user input


## Running the Vertex AI Application

- Create an Agent Builder and Dialogflow application using a sample file (RAG approach)

- cd into VertexAI_Agent

- Execute the app.py inside a venv (after installing the required packaged using the requirements.txt file)

## Glimpse into Gemini applications

- A series of simple gemini applications are included 

- ATS / Resume Analysis 

        - Create a conda venv using python 3.10 version

            conda create -n ats_env python=3.10

        - Activate the environment

            conda activate ats_env

        - Install the libraries using requirements.txt file
        
        - Run the code using the below command

            streamlit run ats.py

- Chat Application

        - Create a conda venv using python 3.10 version

            conda create -n chat_env python=3.10

        - Activate the environment

            conda activate chat_env

        - Install the libraries using requirements.txt file
        
        - Run the code using the below command

            streamlit run chat.py