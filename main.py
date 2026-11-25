"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one original sick-day excuse, under 200 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

EXCUSE = (
    "My neighbour's parrot learned my alarm sound and has been screaming "
    "it since 5am, so technically I've already worked three shifts today "
    "and I'm taking one back."
)


def main() -> None:
    # One breath, one excuse: the laugh lands on "taking one back".
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
