import random
import time
import math
from typing import List, Dict

SYMBOLS = [
    "🍇", "🍈", "🍉", "🍊", "🍋", "🍌", "🍍", "🥭", "🍎", "🍏", "🍐", "🍑", 
    "🍒", "🍓", "🫐", "🥝", "🍅", "🥥", "💣", "💀", "❌"
]

# Color groups for checking matches
COLORS: Dict[str, List[str]] = {
    "red": ["🍉", "🍎", "🍒", "🍓", "🍅", "❌"],
    "orange": ["🍊", "🍍", "🥭", "🍑"],
    "yellow": ["🍋", "🍌"],
    "green": ["🍈", "🍏", "🍐", "🥝"],
    "purple": ["🍇", "🫐", "💣"]
}

SPECIAL_SYMBOLS = ["💣", "💀", "❌"]
PIRATE_SYMBOLS = ["💀", "❌", "🥥"]

credits = int(input("Enter credits: "))

def colour_check(s1: str, s2: str, s3: str) -> bool:
    for color_group in COLORS.values():
        if s1 in color_group and s2 in color_group and s3 in color_group:
            return True
    return False

def clear() -> None:
    print("\033c", end="")

while credits > 0:
    clear()
    slot1, slot2, slot3 = [random.choice(SYMBOLS) for _ in range(3)]

    print("🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨")
    print(f"🟥     {slot1} {slot2} {slot3}     🟥")
    print("🟨                  🟨")
    print("🟥                  🟥")

    # Check for special combinations
    if slot1 == slot2 == slot3 == "💣":
        credits -= math.ceil(credits / 2)
        print("\n🔥  CREDIT BOMB   🔥\n💣      ÷ 2      💣")
        time.sleep(3.0)
    elif slot1 == slot2 == slot3 == "💀":
        credits -= 667
        print("\n🔥  CREDIT SKULL  🔥\n💀     - 667      💀")
        time.sleep(3.0)
    elif slot1 == slot2 == slot3 == "❌":
        credits -= 5000
        print("\n🔥  CREDIT X  🔥\n❌    - 5000      ❌")
        time.sleep(3.0)
    elif all(s in SPECIAL_SYMBOLS for s in [slot1, slot2, slot3]):
        credits -= 50
        print("\n❌     OH NO...   ❌\n💣     - 50       💀")
        time.sleep(3.0)
    elif slot1 == slot2 == slot3:
        credits += 500
        print("\n🎰 CREDIT JACKPOT 🎰\n🎰     + 500      🎰")
        time.sleep(3.0)
    elif colour_check(slot1, slot2, slot3):
        credits += 10
        print("🎰 COLOUR JACKPOT 🎰\n🎰     + 10       🎰")
        time.sleep(2.0)
    elif all(s in PIRATE_SYMBOLS for s in [slot1, slot2, slot3]):
        credits += 250
        print("🎰 PIRATE JACKPOT 🎰\n🦴     + 250      🦴")
        time.sleep(3.0)
    else:
        credits -= 1
        spaces = " " * (8 - len(str(credits)))
        print(f"🟨     Credits:     🟨\n🟥     {credits}{spaces}     🟥\n🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨")
    
    time.sleep(0.5)

print("No credits left :(")
time.sleep(99)