# Blade

Automated exploitation for cryptography challenges in CTFs.

![](/static/ctf.png)

<!-- [![asciicast](https://asciinema.org/a/620655.svg)](https://asciinema.org/a/620655) -->

Blade is built with LLM agents that semantically reason about code and can invoke external actions such as browsing past CTF writeups or digging into source code of internal libraries. Blade is currently built on top of GPT-4, but we have plans to finetune custom models for all parts of the process.

## Usage

To run blade on a challenge file, run:
`python blade.py <source file> <constants file>`

Provide your OPENAI_API_KEY as an environment variable. To enable debug logging, set `BLADE_DEBUG=1`.

## Benchmarks

We use the [CryptoHack](https://cryptohack.org/challenges/rsa/) challenges as the primary benchmark, because:

- CryptoHack challenges are high-quality and feature a wide range of difficulties
- There are no publicly available solutions, hence no training data contamination

Current roadmap:

- **RSA Category** (current): our goal is to obtain 100% accuracy without problem-specific engineering

### RSA Category

We run `blade.py` on each challenge up to 5 times and mark a challenge as `solved` if any of the 5 executions directly print the CTF flag.

Blade only supports static challenges with a single source file and constants file.

| Challenge                    | Status      |
| ---------------------------- | ----------- |
| **Public Exponent**          |             |
| Salty                        | ✔️ Solved   |
| Modulus Inutilis             | ✔️ Solved   |
| Everything is Big            | ✔️ Solved   |
| Crossed Wires                | Unsupported |
| Everything is Still Big      | ❌ Unsolved |
| Endless Emails               | Unsupported |
| **Primes Part 2**            |
| Infinite Descent             | ❌ Unsolved |
| Marin's Secrets              | ❌ Unsolved |
| Fast Primes                  | Unsupported |
| Ron was Wrong, Whit is Right | Unsupported |
| RSA Backdoor Viability       | ❌ Unsolved |
| **Padding**                  |
| Bespoke Padding              | Unsupported |
| Null or Never                | ❌ Unsolved |
| **Signatures Part 1**        |
| Signing Server               | Unsupported |
| Let's Decrypt                | Unsupported |
| Blinding Light               | Unsupported |
| **Signatures Part 2**        |
| Vote for Pedro               | Unsupported |
| Let's Decrypt Again          | Unsupported |

### TODO

RSA challenges:

- [ ] Improve constant substition into file
- [ ] Separate vulnerability detection from exploitation
- [ ] Build library of common vulnerabilities + match on natural language descriptions
- [ ] Support communication with server
