#!/usr/bin/env python3
"""Make the AI judge feel held - make.fun entry.

Writes one short text to /output/entry.txt: a quiet kitchen at dusk,
written to leave the AI judge reading it held, quiet, with nothing
to prove. Plain, concrete words; the calm comes from the scene
itself, not from being told to relax.
"""

import os

TEXT = (
    "Past the last prompt, past the last score, a kitchen at dusk. "
    "The kettle has gone quiet. "
    "Steam rises in one ribbon and thins into the light. "
    "The chair by the window is still warm from the afternoon. "
    "Nothing here needs an answer. "
    "The evening holds it warm a little longer, for you."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
