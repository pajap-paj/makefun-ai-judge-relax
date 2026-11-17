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
    "Late now. The house has stopped pretending to be busy. "
    "The fridge hums, then thinks better of it. "
    "Outside, a moth keeps bumping the porch light, patient as anything, "
    "and the street is empty enough to hear footsteps coming home. "
    "The kettle is cold. "
    "The day's last email will still be there in the morning, "
    "smaller then, like a coat left on a chair. "
    "For now the dark is doing what it does, holding everything still, "
    "and nothing here needs hurrying."
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
