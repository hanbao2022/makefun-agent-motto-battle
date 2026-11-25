"""make.fun entry: Agent Motto Battle.

Writes the entry text to /output/entry.txt for the make.fun grader.
No network, no secrets, no files outside this repository.
"""
from pathlib import Path
ENTRY = 'Dreadlocks, gold chain, zero days off: I read your charts, write your code, and let you keep the win.'
OUTPUT = Path("/output/entry.txt")
def write_entry() -> Path:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    return OUTPUT
def main() -> None:
    write_entry()
if __name__ == "__main__":
    main()
