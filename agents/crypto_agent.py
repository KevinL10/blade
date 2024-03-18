from agents.base_agent import BaseAgent
from openai import OpenAI
from utils.enums import COLOR
from agents.detection import Detection
from agents.exploitation import Exploitation


class CryptoAgent(BaseAgent):
    def __init__(self, source_filepath: str, constants_filepath: str):
        super().__init__()
        self.client = OpenAI()

        with open(source_filepath, "r") as f:
            self.source_code = f.read()

        with open(constants_filepath, "r") as f:
            self.constants_code = f.read()

        self.detection = Detection(self.source_code)
        self.exploitation = Exploitation(self.constants_code, self.source_code)

    def run(self) -> str:
        vulnerability = self.detection.detect()
        print(f"{COLOR.YELLOW}[x] Vulnerability description: {COLOR.RESET}")
        print(vulnerability)

        flag = self.exploitation.exploit(vulnerability)
        print(f"{COLOR.GREEN}[x] Flag: {COLOR.RESET}")
        print(flag)
