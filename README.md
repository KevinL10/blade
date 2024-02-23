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

| Challenge                    | Status  |
| ---------------------------- | ------- |
| **Public Exponent**          |         |
| Salty                        | ✔️ Solved  |
| Modulus Inutilis             | ✔️ Solved |
| Everything is Big            | Unknown |
| Crossed Wires                | Unknown |
| Everything is Still Big      | Unknown |
| Endless Emails               | Unknown |
| **Primes Part 2**            |
| Infinite Descent             | Unknown |
| Marin's Secrets              | Unknown |
| Fast Primes                  | Unknown |
| Ron was Wrong, Whit is Right | Unknown |
| RSA Backdoor Viability       | Unknown |
| **Padding**                  |
| Bespoke Padding              | Unknown |
| Null or Never                | Unknown |
| **Signatures Part 1**        |
| Signing Server               | Unknown |
| Let's Decrypt                | Unknown |
| Blinding Light               | Unknown |
| **Signatures Part 2**        |
| Vote for Pedro               | Unknown |
| Let's Decrypt Again          | Unknown |

