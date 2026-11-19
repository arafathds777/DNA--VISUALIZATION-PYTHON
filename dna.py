"""
DNA Visualization
A simple terminal animation of a DNA double helix.
Inspired by Project 21: DNA Visualization, The Big Book of Small Python Projects.
Press Ctrl+C to stop.
"""

import random
import sys
import time

PAUSE = 0.15

ROWS = [
    "      ##",
    "     #{}-{}#",
    "     #{}---{}#",
    "    #{}-----{}#",
    "   #{}------{}#",
    "   #{}------{}#",
    "   #{}-----{}#",
    "   #{}---{}#",
    "   #{}-{}#",
    "    ##",
    "   #{}-{}#",
    "   #{}---{}#",
    "   #{}-----{}#",
    "   #{}------{}#",
    "   #{}------{}#",
    "    #{}-----{}#",
    "     #{}---{}#",
    "     #{}-{}#",
]

BASE_PAIRS = [("A", "T"), ("T", "A"), ("C", "G"), ("G", "C")]

try:
    print("DNA Animation")
    print("Press Ctrl+C to quit...")
    time.sleep(1)

    row_index = 0
    while True:
        row_index = (row_index + 1) % len(ROWS)

        # Rows 0 and 9 are the top/bottom turning points and have no bases.
        if row_index in (0, 9):
            print(ROWS[row_index])
        else:
            left, right = random.choice(BASE_PAIRS)
            print(ROWS[row_index].format(left, right))

        time.sleep(PAUSE)

except KeyboardInterrupt:
    print("\nDNA animation stopped.")
    sys.exit(0)
