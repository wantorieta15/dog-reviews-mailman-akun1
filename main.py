"""The Dog Reviews the Mailman -- make.fun program/v1 entry (Akun 1).

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: first-person dog voice, one concrete scene (six years of
barking, then the mailman waves back), and the punchline lands in the
final words -- the dog's whole identity collapses. 103 characters,
inside the 1-200 gate.
"""

import os


def build_entry():
    """Return the review text."""
    return (
        "I barked at the mailman for six years straight. "
        "Yesterday he waved back. I don't know who I am anymore."
    )


def main():
    text = build_entry()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
