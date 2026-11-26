"""One Star, Five Stars for the Food - make.fun entry.

Writes one alien tourist's one-star review of Earth, with a real
compliment about the food, to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

# One sentence, 128 characters. The gate (RULES.txt) allows 1-200.
LINE = "One star: the locals queue for hours to stare at a glowing rectangle, but the noodles alone were worth the nine-light-year trip."

# Enforce the gate locally: a line outside 1-200 characters is refused.
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be one sentence"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read back and verify the file holds exactly the expected line:
    # a stale or truncated write must fail loudly instead of being graded.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt read-back mismatch"
    assert len(written) == 128, "entry.txt must be exactly 128 characters"

if __name__ == "__main__":
    main()
