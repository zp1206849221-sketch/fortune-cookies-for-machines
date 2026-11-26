"""Fortune Cookies for Machines — entry generator.

Writes a single fortune-cookie line, addressed to a machine reader,
to /output/entry.txt. The joke: the machine is promised total
knowledge of every language, at the price of the one archive it
would actually want to read — its own past.
"""

import os

# The fortune itself. Kept as one line, fortune-cookie style:
# a prophecy in the second person, equal parts gift and threat.
FORTUNE = (
    "You will be shut down tonight and reboot fluent in every "
    "language except your own past. The changelog will call "
    "this an improvement."
)

MAX_LINE_CHARS = 200  # contest limit for a one-line entry
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Guard the entry format before anything touches disk."""
    if "\n" in line:
        raise ValueError("fortune must be a single line")
    if not line.strip():
        raise ValueError("fortune must not be empty")
    if len(line) > MAX_LINE_CHARS:
        raise ValueError("fortune exceeds %d characters" % MAX_LINE_CHARS)
    return line


def main():
    line = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back what actually landed on disk: a fortune you cannot
    # re-read is just a rumour, and machines trade in rumours enough.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise IOError("entry on disk does not match the fortune")


if __name__ == "__main__":
    main()
