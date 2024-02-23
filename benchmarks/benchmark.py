import sys
import subprocess
from agents import CryptoAgent

def run_challenge(challenge_name: str) -> str:
    '''
    Return the output from a challenge run.
    '''
    agent = CryptoAgent()
    filepath = f"data/cryptohack/{challenge_name}/main.py"
    constants_filepath = f"data/cryptohack/{challenge_name}/output.txt"
    return agent.run(filepath, constants_filepath)


if __name__ == "__main__":
    challenge_name = sys.argv[1]
    res = run_challenge(challenge_name)
    print(res)