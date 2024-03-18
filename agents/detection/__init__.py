from openai import OpenAI 

class Detection:
    '''
    Detects vulnerabilities in the given source code
    '''
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.client = OpenAI()

    def detect(self) -> str:
        '''
        Returns a description of any found vulnerabilities with as much
        detail as possible. This description is passed to the exploitation engine
        to generate a functional script.
        '''

        completion = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages = [
                {"role": "system", "content": "You are an expert in cryptography and SageMath"},
                {"role": "user", "content": f"""
You are provided with the source code related to an RSA cryptography problem, enclosed within the triple backticks below. Your task is to analyze the code and identify the cryptographic vulnerability to recover the unknown FLAG variable.

Please note:
- There is a known vulnerability that can be exploited without extensive brute-force attacks on the RSA parameters.
- Focus on the unique construction of the RSA values presented in the code, such as bit lengths and algebraic relationships

Approach the problem methodically, breaking down your analysis into clear, step-by-step explanations. Your response should be concise and describe the exact vulnerability required to recover the FLAG variable.
```
{self.source_code}                 
```              
"""}
            ]
        )
        return completion.choices[0].message.content
