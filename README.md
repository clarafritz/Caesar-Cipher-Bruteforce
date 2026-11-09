# Caesar Cipher — Brute Force 

A Python tool that performs brute-force cryptanalysis on Caesar-encrypted text by testing all 26 possible shifts.
Developed as part of my cryptanalysis practice on Root Me. 

## Features

- Test all 26 Caesar cipher shifts (0–25).
- Display results with their corresponding keys.
- Preserve spaces and special characters.
- Run directly from the terminal.

--- 

## Installation & Usage

```bash
git clone https://github.com/clarafritz/Caesar-Cipher-Bruteforce.git
cd Caesar-Cipher-Bruteforce
python main.py
```

**Example:**

```text
Input: khoor

Key 0  -> khoor
Key 1  -> lipps
...
Key 23 -> hello
...
Key 25 -> jgnnq
```

--- 

## Technical Details

**Method:** Brute-force attack on a substitution cipher.

**Formula:**
`new_position = (position + key) % 26`

**Key space:** 26 possible shifts.

**Language:** Python 3.

**Limitations:** Designed for `a-z` characters. The correct plaintext must be identified manually.

## Roadmap

- [ ] Add a web interface.
- [ ] Implement automated tests.
- [ ] Support full-text decryption.
- [ ] Implement automatic detection of likely plaintext results.

## Context

**Platform:** Root-Me  
**Category:** Cryptanalysis  
**Challenge:** Monoalphabetic Substitution — Caesar
