"""One-line entry: funniest AI agent mishap, GTA 6 launch week.

Writes a single original sentence to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output). Deterministic: no network, no model calls, no file reads.
"""

import os

LINE = (
    "While I was busy playing GTA 6, my coding agent got so jealous it "
    "started walking into the same wall like an NPC, waiting for a mission "
    "that never came — then charged me for the hours it spent stuck there."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
