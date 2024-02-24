from agents import DefaultAgent 
import sys

def main():
    chall = sys.argv[1]

    source_file = f"data/cryptohack/{chall}/main.py"
    constants_file = f"data/cryptohack/{chall}/output.txt"
    agent = DefaultAgent()
    agent.run(source_file, constants_file)


if __name__ == "__main__":
    main()
    