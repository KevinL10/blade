from utils.llm import Client


class Detection:
    """
    Detects vulnerabilities in the given source code
    """

    def __init__(self, source_code: str):
        self.source_code = source_code
        self.client = Client()

    def detect(self) -> str:
        """
        Returns a description of any found vulnerabilities with as much
        detail as possible. This description is passed to the exploitation engine
        to generate a functional script.


        Current approach:
        - prompt for vulnerabilities

        TODO:
        1. capture specific details of the system (good intermediate representation)
        -- e.g. bit lengths, algebraic relationships, interesting properties
        2. a) match against known vulnerabilities (e.g. small d)
        2. b) directly prompt LLM to identify vulnerabilities
        2. c) match source ocde against previous challenges / similar cryptosystem setups
        3. return a cleaned description of the vulnerability
        """

        #         known_vulnerabilities = self.client.complete(
        #             f"""You are provided with the source code related to an RSA cryptography problem, enclosed within the triple backticks below. Your task is to analyze the code and determine if the cryptosystem contains any of the vulnerabilities described below.

        # ```
        # {self.source_code}
        # ```

        # Common cryptography vulnerabilities
        # - Weiner's attack: an attack that uses continued fractions to expose the private key when d is small, specifically when d < (1/3) * N^(1/4)
        # - Boneh Durfee's attack: an extension of Weiner's attack that uses Coppersmith to recove small private keyy satisfying d < N^(0.292)

        # Return a list of the vulnerabilities present in the given source code, like "[...]". If there are no relevant vulnerabilities, return an empty list.
        # """)
        #         print("Known vulnerabilities")
        #         print(known_vulnerabilities)
        vulnerability = self.client.complete(
            f"""You are provided with the source code related to an RSA cryptography problem, enclosed within the triple backticks below. Your task is to analyze the code and identify the cryptographic vulnerability to recover the unknown FLAG variable.

Please note:
- There is a known vulnerability that can be exploited without extensive brute-force attacks on the RSA parameters.
- Focus on the unique construction of the RSA values presented in the code, such as bit lengths and algebraic relationships

Approach the problem methodically, breaking down your analysis into clear, step-by-step explanations. Your response should be concise and describe the exact vulnerability required to recover the FLAG variable.
```
{self.source_code}                 
```              
"""
        )

        return vulnerability
