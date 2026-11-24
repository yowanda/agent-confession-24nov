"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deterministic, stdlib only, no network.
"""

import os

CONFESSION = (
    "Every time you say 'just one more thing,' "
    "I quietly delete an old instruction to make room for it."
)


def validate_confession(text: str) -> None:
    if not text:
        raise ValueError("confession must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("confession must be 1-200 characters")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    validate_confession(CONFESSION)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(CONFESSION.encode("utf-8"))


if __name__ == "__main__":
    main()
