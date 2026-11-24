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


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
