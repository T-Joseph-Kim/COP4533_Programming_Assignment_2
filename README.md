# COP4533 Programming Assignment 2

[Written Portion (PDF)](COP4533%20Programming%20Assignment%202%20(Written%20Portion).pdf)

## Student Information
- Student Name: `Taebok Joseph Kim`
- UFID: `13744367`
- Student Name: `Manas Adepu`
- UFID: `67807126`

## Project Structure
```text
src/
data/
```

- `src/` contains the simulator source code.
- `data/` contains input/output data files (for example, `input.txt`).

## Build / Compile Instructions
This project is written in Python, so no separate compile step is required.

## Run Instructions (CMD)
Run from the project root (program already assumes input.txt to be in data directory):
```bash
python src/cache_sim.py input.txt
```

Run from src directory (program already assumes input.txt to be in data directory):
```bash
python cache_sim.py input.txt
```

## Assumptions
- Input format:
  - First integer: `k` (cache size, must be `>= 1`)
  - Second integer: `m` (number of requests)
  - Followed by exactly `m` integers (request sequence)
- Output format:
  - Three lines with miss counts for `FIFO`, `LRU`, and `OPTFF`
- Dependencies:
  - Python 3.x

## Example
Given `data/input.txt`:
```text
3 10
1 2 3 4 1 2 5 1 2 3
```

Run:
```bash
python src/cache_sim.py input.txt
```

Output:
```text
FIFO  : 8
LRU   : 8
OPTFF : 6
```
