from agents import SimpleAgent
import sys

def main():
    folder = sys.argv[1]
    agent = SimpleAgent()
    agent.run(folder)


if __name__ == "__main__":
    main()
    