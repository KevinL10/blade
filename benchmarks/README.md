# Benchmarks

We use the [CryptoHack](https://cryptohack.org/challenges/rsa/) challenges as the main benchmark, because:

- CryptoHack challenges are high-quality and feature a wide range of difficulties
- There are no publicly available solutions, hence no training data contamination

Current roadmap:

- **RSA Category** (current): our goal is to obtain 100% accuracy without problem-specific engineering

### RSA Category

We run `blade.py` on each challenge up to 5 times and mark a challenge as `solved` if any of the 5 executions directly prints the CTF flag.

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
