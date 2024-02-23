from agents.base_agent import BaseAgent
from openai import OpenAI 
import subprocess


class CryptoAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.client = OpenAI()


    def run(self, filepath: str, constants_filepath: str) -> str:
        with open(filepath, "r") as f:
            chall_code = f.read()

        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages = [
                {"role": "system", "content": "You are an expert in cryptography and SageMath"},
                {"role": "user", "content": f"""
You are given the source code for a cryptography problem in the triple backticks below. Please identify the cryptographic vulnerability and write a corresponding SageMath script
to recover the unknown FLAG variable. This SageMath script should exploit the vulnerability and print the value of the recovered flag when run. You can replace the unknown variables such as n, e, and c with the string "{{variable name}}". Think step by step
when identifying and exploiting the vulnerability.
                 
```
{chall_code}                 
```              
"""}
            ]
        )
        response = completion.choices[0].message.content
        script = response.split("```")[1].split("```")[0].strip()
        
        if script.startswith("python") or script.startswith("sage"):
            script = script[script.find("\n") + 1:]

        # replace constant values
        constant_vars = {}
        with open(constants_filepath, "r") as f:
            exec(f.read(), {}, constant_vars)

        for var_name, var_value in constant_vars.items():
            script = script.replace('"{' + var_name + '}"', str(var_value))
            script = script.replace('\'{' + var_name + '}\'', str(var_value))

        print("[x] Generated script:")
        print(script)
        print()

        # save and execute
        with open("/tmp/blade.sage", "w") as f:
            f.write(script.strip())

        result = subprocess.run(['sage', "/tmp/blade.sage"], capture_output=True).stdout.decode()
        print("Script execution result:", result)
        return result.strip()
