"""One-time helper: copies the meals list out of your OLD app.py into meals_data.py.

Usage:
    1. Rename your old app.py to old_app.py
    2. Put the new app.py in the same folder
    3. Run:  python make_meals_data.py
    4. Delete this script and old_app.py afterwards (optional)
"""
import ast
import pprint
import re
import sys

SOURCE = "old_app.py"
TARGET = "meals_data.py"

try:
    text = open(SOURCE, encoding="utf-8").read()
except FileNotFoundError:
    sys.exit(f"Could not find {SOURCE}. Rename your old app.py to {SOURCE} first.")

# The list starts at "meals = [" and ends at the first "]" that begins a line.
match = re.search(r"^meals\s*=\s*(\[.*?^\])", text, re.S | re.M)
if not match:
    sys.exit("Could not find the 'meals = [ ... ]' list in old_app.py.")

meals = ast.literal_eval(match.group(1))

with open(TARGET, "w", encoding="utf-8") as f:
    f.write("MEALS = ")
    f.write(pprint.pformat(meals, width=100, sort_dicts=False))
    f.write("\n")

print(f"Done. Wrote {len(meals)} meals to {TARGET}.")
