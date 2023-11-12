# Blade 

Automated vulnerability detection for CTF challenges, inspired by [Katana](https://github.com/JohnHammond/katana).

Blade is built with LLM agents that can semantically reason about code and invoke external actions such as browsing past CTF writeups or digging into source code of internal libraries. 

We currently use the GPT-4 model from OpenAI. In the future, we plan to finetune a custom model based on public [vulnerability](https://arxiv.org/pdf/2304.00409.pdf) [datasets](https://www.inf.u-szeged.hu/~ferenc/papers/JSVulnerabilityDataSet/).

This repository serves as a public experiment to see how LLMs perform on complex security challenges. If you're interested in building custom tools and agents, or would like to help in any other way, please feel free to create a GitHub issue or email `root@vulnix.dev`!

## Usage

`python main.py <folder>`

Provide your OPENAI_API_KEY as an environment variable.

## Roadmap
#### General
- [] Create a pip package for CLI usage
- [] Finetuned model on public security vulnerability datasets

#### Agents
- [] Direct OpenAI wrapper with prompt-tuning
- [] Zero-shot ReAct agent
- [] Interactive agents for guiding vulnerability analysis

#### Tools
- [] Search through indexed CTF writeups and CVEs
- [] Search within codebase
- [] Live web browsing
- [] Code execution
