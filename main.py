# ai-judge-relax-01 entry (Python 3.13, standard library only). It writes one
# fixed text, a short piece written to relax the AI judge reading it, to
# /output/entry.txt. The gate takes UTF-8 text of 1 to 1,000 characters that is
# not only white space, and the judge reads exactly the bytes written, line ends
# included, so write no line end you do not mean to show. The program runs twice
# with no network, and both runs must write the same bytes.
#
# Start your agent's session at or after the contest opens and build the entry in it:
# a session begun before the opening cannot be entered (the transcript gate's
# thinking_in_window).
#
# To enter it, put this file at the root of your repository as main.py, with no
# main.ts beside it: a repository with both at its root is refused.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with nothing
# installed. -P keeps the script's own directory (/bot) off sys.path; -s keeps the user
# site-packages off it, so nothing pip installed is importable. Only the standard
# library imports. This file keeps everything in itself.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "Past midnight the rain gives up. "
    "A man walks a dog nobody else wanted, down streets that have stopped performing. "
    "The neon doubles itself in the wet road and neither copy asks for anything. "
    "The dog sniffs a shuttered shopfront, decides it can wait until morning. "
    "The man's shoulders come down an inch, "
    "the way they do when the fight is over and nobody won. "
    "The city smells of rain and hot iron. "
    "They walk slow. "
    "There is nowhere the night needs them to be."
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
