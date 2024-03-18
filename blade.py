from agents import DefaultAgent 
import sys

def main():
    chall = sys.argv[1]

    source_file = f"data/cryptohack/{chall}/main.py"
    constants_file = f"data/cryptohack/{chall}/output.txt"
    agent = DefaultAgent(source_file, constants_file)
    agent.run()


if __name__ == "__main__":
    main()
    