from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.output_parsers import PydanticOutputParser
from langchain.chains.openai_functions import get_openai_output_parser

from models import VulnerabilityReport
from utils import load_folder_as_chunks
from utils.enums import COLOR

import langchain
import time
import logging
import os

langchain.debug = os.environ.get("BLADE_DEBUG", False)

logging.basicConfig(level=logging.INFO, format=f'[{COLOR.LIGHT_BLUE}%(asctime)s{COLOR.RESET}] [{COLOR.LIGHT_GREEN}%(levelname)s{COLOR.RESET}] %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger("AgentLogger")

def display_vulnerability_info(vulnerability):
    logger.critical(f'{COLOR.BOLD_RED}Detected {vulnerability["type"]} in {vulnerability["location"]}{COLOR.RESET}')
    print("```")
    print(vulnerability["code"])
    print("```")
    print(vulnerability["description"])

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
        self.chat = self.chat.bind(functions=[{
            "name": "analyze_vulnerabilities", 
            "description": "Analyze the code and return a list of security vulnerabilities.",
            "parameters": VulnerabilityReport.model_json_schema()
        }])
        self.parser = get_openai_output_parser((VulnerabilityReport, ))
        self.agent = self.chat | self.parser


    def run(self, folder):
        start_time = time.time()
        documents = load_folder_as_chunks(folder)
        vulnerabilities = []

        with get_openai_callback() as cb:
            for i, document in enumerate(documents):
                logger.info(f'Analyzing {document.metadata["source"]} ({i+1}/{len(documents)})')

                messages = [
                    SystemMessage(
                        content="You are an expert cybersecurity analyst tasked with finding security vulnerabilities."
                    ),
                    HumanMessage(
                        content="""Given the code below delimited by triple backticks, analyze the code for any critical security OWASP web vulnerabities that may lead to remote-code execution or other severe consequences. Ignore all non-critical vulnerabilities such as lack of encryption, error handling, logging of data, or sensitive data exposure. 
List each vulnerability one-by-one in a JSON format, with the type of vulnerability, surrounding 3 lines of code, and a short description of the context. If there are no critical vulnerabilities, simply return an empty list. 
Think step by step and carefully analyze each line of code. Only list vulnerabilities for which you are certain of and have found evidence in code. If the vulnerability depends on a hypothetical condition that is unmet, do not list the vulnerability.
        ```
        {code}
        ```""".format(code=document.page_content)
                    ),
                ]
                output = self.agent.invoke(messages)
                for vulnerability in output["vulnerabilities"]:
                    vulnerability["location"] = document.metadata["source"]
                    display_vulnerability_info(vulnerability)

                vulnerabilities.extend(output["vulnerabilities"])
        
            display_color_ansi = COLOR.GREEN if len(vulnerabilities) == 0 else COLOR.RED
            logger.info(f'{display_color_ansi}Found {len(vulnerabilities)} {"vulnerability" if len(vulnerabilities) == 1 else "vulnerabilities"} in {(time.time() - start_time)}s{COLOR.RESET}')
            logger.info(f"Total Cost (USD): ${cb.total_cost}") 