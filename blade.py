from agents import DefaultAgent 
import sys

def main():
    source_file = sys.argv[1]
    constants_file = sys.argv[2]
    agent = DefaultAgent()
    agent.run(source_file, constants_file)


if __name__ == "__main__":
    main()
    