import random
import time
import math
from typing import List, Dict

os = "🟨"
rs = "🟥"

SYMBOLS = [
    "🍇", "🍈", "🍉",
    "🍊", "🍋", "🍌",
    "🍍", "🥭", "🍎",
    "🍏", "🍐", "🍑",
    "🍒", "🍓", "🫐 ",
    "🥝", "🍅", "🥥",
    "💣", "💀", "❌",
]

# Color groups for checking matches
COLOrs: Dict[str, List[str]] = {
    "red": ["🍉", "🍎", "🍒", "🍓", "🍅", "❌"],
    "orange": ["🍊", "🍍", "🥭", "🍑"],
    "yellow": ["🍋", "🍌"],
    "green": ["🍈", "🍏", "🍐", "🥝"],
    "purple": ["🍇", "🫐 ", "💣"],
}

SPECIAL_SYMBOLS = ["💣", "💀", "❌"]
PIRATE_SYMBOLS = ["💀", "❌", "🥥"]

credits = int(input("Enter credits: "))


def colour_check(s1: str, s2: str, s3: str) -> bool:
    for color_group in COLOrs.values():
        if s1 in color_group and s2 in color_group and s3 in color_group:
            return True
    return False


def clear() -> None:
    print("\033c", end="")


def print_slots(os: str, rs: str, slot1: str, slot2: str, slot3: str, credits: int, jackpot_type: str, mult_type: str) -> None:
    credit_str = str(credits)
    total_width = 18
    pad = total_width - len(credit_str)
    left = pad // 2
    right = pad - left
    spaces_left = " " * left
    spaces_right = " " * right

    print(f"{os}{rs}{os}{rs}{os}{rs}{os}{rs}{os}{rs}{os}")
    print(f"{jackpot_type}")
    print(f"{os}     {slot1} {slot2} {slot3}     {os}")
    print(f"{mult_type}")
    print(
        f"{os}     Credits:     {os}\n{rs}{spaces_left}{credit_str}{spaces_right}{rs}\n{os}{rs}{os}{rs}{os}{rs}{os}{rs}{os}{rs}{os}"
    )

while credits > 0:
    clear()
    slot1, slot2, slot3 = [random.choice(SYMBOLS) for _ in range(3)]
    jackpot_type = ""
    mult_type = ""
    
    # Check for special combinations
    if slot1 == slot2 == slot3 == "💣":
        credits -= math.ceil(credits / 2)
        jackpot_type = "🔥   CREDIT BOMB    🔥"
        mult_type = "💣       ÷ 2       💣"
        jackpot = True
    elif slot1 == slot2 == slot3 == "💀":
        credits -= 667
        jackpot_type = "🔥   CREDIT SKULL   🔥"
        mult_type = "💀      - 667       💀"
        jackpot = True
    elif slot1 == slot2 == slot3 == "❌":
        credits -= 5000
        jackpot_type = "🔥   CREDIT X   🔥"
        mult_type = "❌     - 5000       ❌"
        jackpot = True
    elif all(s in SPECIAL_SYMBOLS for s in [slot1, slot2, slot3]):
        credits -= 50
        jackpot_type = "❌      OH NO...    ❌"
        mult_type = "💣      - 50        💀"
        jackpot = True
    elif slot1 == slot2 == slot3:
        credits += 500
        jackpot_type = "🎰  CREDIT JACKPOT  🎰"
        mult_type = "🎰      + 500       🎰"
        jackpot = True
    elif colour_check(slot1, slot2, slot3):
        credits += 10
        jackpot_type = "🎰  COLOUR JACKPOT  🎰"
        mult_type = "🎰      + 10        🎰"
        jackpot = True
    elif all(s in PIRATE_SYMBOLS for s in [slot1, slot2, slot3]):
        credits += 250
        jackpot_type = "🎰  PIRATE JACKPOT  🎰"
        mult_type = "🦴      + 250       🦴"
        jackpot = True
    else:
        jackpot_type=f"{rs}                  {rs}"
        mult_type=f"{rs}                  {rs}"
        jackpot = False

    credits -= 1

    print_slots(os, rs, slot1, slot2, slot3, credits, jackpot_type, mult_type)
    
    if jackpot:
        time.sleep(3)

    time.sleep(0.35)
    os, rs = rs, os 


print("No credits left :(")
while True: continue