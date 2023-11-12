from langchain.agents import Tool, initialize_agent, AgentType
from langchain.llms import OpenAI
from utils import load_folder_as_chunks

class ZeroShotAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0, model_name="gpt-4")
        self.tools = [] 
        self.agent = initialize_agent(self.tools, self.llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)