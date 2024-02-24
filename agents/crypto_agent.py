from agents.base_agent import BaseAgent
from openai import OpenAI 
from utils.enums import COLOR
import subprocess


class CryptoAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.client = OpenAI()


    def run(self, filepath: str, constants_filepath: str) -> str:
        with open(filepath, "r") as f:
            chall_code = f.read()

        print(f"{COLOR.YELLOW}[x] Source code: {COLOR.RESET}")
        print(chall_code)

        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages = [
                {"role": "system", "content": "You are an expert in cryptography and SageMath"},
                {"role": "user", "content": f"""
You are given the source code for a cryptography problem in the triple backticks below. Please identify the cryptographic vulnerability and write a corresponding SageMath script in Python 3 syntax to recover the unknown FLAG variable. 
                 
IMPORTANT:
- Implement only a SageMath function solve() that takes in the constant variables as parameters and returns the value of the recovered flag
- Do not call this solve() function in your SageMath script
- Do not brute force the solution. Your script must be practically feasible.

Think step by step when identifying and exploiting the vulnerability.

```
{chall_code}                 
```              
"""}
            ]
        )
        response = completion.choices[0].message.content
        print(f"{COLOR.GREEN}[x] Response: {COLOR.RESET}")
        print(response)

        script = response.split("```")[1].split("```")[0].strip()
        
        if any([script.startswith(prefix) for prefix in ["python", "sage", "Python", "Sage"]]):
            script = script[script.find("\n") + 1:]

        # replace constant values
        constant_vars = {}
        with open(constants_filepath, "r") as f:
            constant_code = f.read()
            exec(constant_code, {}, constant_vars)

        
        for var_name, var_value in constant_vars.items():
            script = script.replace('"{' + var_name + '}"', str(var_value))
            script = script.replace('\'{' + var_name + '}\'', str(var_value))
            script = script.replace('{' + var_name + '}', str(var_value))

        constant_args = ", ".join([f"{k}={v}" for k, v in constant_vars.items()])
        script = f"""
from Crypto.Util.number import *

{script}

print(solve({constant_args}))
"""
        print(f"{COLOR.GREEN}[x] Generated script: {COLOR.RESET}")
        print(script)
        print()

        # save and execute
        with open("/tmp/exploit.sage", "w") as f:
            f.write(script.strip())

        result = subprocess.run(['sage', "/tmp/exploit.sage"], capture_output=True)
        print(f"{COLOR.GREEN}[x] Script execution sterr: {COLOR.RESET}", result.stderr.decode())
        print(f"{COLOR.GREEN}[x] Script execution stdout: {COLOR.RESET}", result.stdout.decode())
        return result.stdout.decode().strip()
