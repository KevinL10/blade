from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from utils import load_folder_as_chunks
import time

class SimpleAgent:
    '''
    SimpleAgent initiates a single model and queries chunks of code at a time. 
    Queries are independent from each other, and thus the agent does not have
    context about code outside of the current snippet. 

    TODO: with the new assistants API, we can query each chunk within a single
    chat session and preserve context without resending past conversation history.
    '''
    def __init__(self):
        self.chat = ChatOpenAI(temperature=0, model_name="gpt-4")


    def run(self, folder):
        start_time = time.time()
        documents = load_folder_as_chunks(folder)
        for chunk in documents:
            messages = [
                SystemMessage(
                    content="You are an expert cybersecurity analyst tasked with finding security vulnerabilities."
                ),
                HumanMessage(
                    content="""Given the code below delimited by triple backticks, list all critical vulnerabilities that you find. Think step by step and carefully analyze each line of code. Be concise but informative.
    ```
    {code}
    ```""".format(code=chunk.page_content)
                ),
            ]
            print(self.chat(messages).content) 
            print('-' * 80)

        print(f"Finished in: {(time.time() - start_time)}s")
    