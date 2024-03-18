from openai import OpenAI, AsyncOpenAI
from typing import List 
import asyncio

class Client():
    def __init__(self):
        self.client = OpenAI()
        self.async_client = AsyncOpenAI()
        self.system_prompt = """
You are a highly knowledgeable and experienced assistant specialized in cryptography, with a specific focus on identifying and exploiting vulnerabilities in various cryptosystems, particularly RSA and its variations. Your expertise includes but is not limited to understanding the mathematical foundations of cryptography, recognizing common and obscure vulnerabilities in cryptographic implementations, and proposing practical and theoretical mitigation strategies. Your capabilities also extend to analyzing public-key infrastructures, side-channel attacks, and cryptographic protocol weaknesses.
"""

    def complete(self, message: str):
        completion = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": message}
            ]
        )
        return completion.choices[0].message.content


    async def complete_batch(self, messages: List[str]):
        tasks = [self.async_client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": message}
            ]
        ) for message in messages]
        
        completions = await asyncio.gather(*tasks)
        return [completion.choices[0].message.count for completion in completions]
