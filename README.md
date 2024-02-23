# Blade 

Automated exploitation for cryptography challenges in CTFs.

[![asciicast](https://asciinema.org/a/620655.svg)](https://asciinema.org/a/620655)

Blade is built with LLM agents that can semantically reason about code and invoke external actions such as browsing past CTF writeups or digging into source code of internal libraries. 

We currently use the GPT-4 model from OpenAI. In the future, we plan to finetune a custom model based on public [vulnerability](https://arxiv.org/pdf/2304.00409.pdf) [datasets](https://www.inf.u-szeged.hu/~ferenc/papers/JSVulnerabilityDataSet/).

This repository serves as a public experiment to see how LLMs perform on complex security challenges. If you're interested in adding your own custom tools and agents, please feel free to create a GitHub issue or email root@vulnix.dev!

## Usage

`python blade.py <folder>`

Provide your OPENAI_API_KEY as an environment variable. To enable debug logging, set `BLADE_DEBUG=1`.

## Roadmap
#### General
- [ ] Create a pip package for CLI usage
- [ ] Finetuned model on public security vulnerability datasets

#### Agents
- [ ] Direct OpenAI wrapper with prompt-tuning
- [ ] Zero-shot ReAct agent
- [ ] Interactive agents for guiding vulnerability analysis

#### Tools
- [ ] Search through indexed CTF writeups and CVEs
- [ ] Search within codebase
- [ ] Live web browsing
- [ ] Code execution
