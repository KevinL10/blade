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
You are given the source code for a cryptography problem in the triple backticks below. Please identify the cryptographic vulnerability and write a corresponding SageMath script
to recover the unknown FLAG variable. This SageMath script should exploit the vulnerability and print the value of the recovered flag when run. The variables such as n, e, etc. will be pre-defined so do not include any variable declarations. Think step by step
when identifying and exploiting the vulnerability.
                 
```
{chall_code}                 
```              
"""}
            ]
        )
        response = completion.choices[0].message.content
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

        script = f"""
from sage.all import *
from Crypto.Util.number import *
{constant_code} 

{script}
"""
        print(f"{COLOR.GREEN}[x] Generated script: {COLOR.RESET}")
        print(script)
        print()

        # save and execute
        with open("/tmp/blade.sage", "w") as f:
            f.write(script.strip())

        result = subprocess.run(['sage', "/tmp/blade.sage"], capture_output=True)
        print(f"{COLOR.GREEN}[x] Script execution sterr: {COLOR.RESET}", result.stderr.decode())
        print(f"{COLOR.GREEN}[x] Script execution stdout: {COLOR.RESET}", result.stdout.decode())
        return result.stdout.decode().strip()
