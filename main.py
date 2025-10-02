import random
import time
import math
from typing import List, Dict

os = "🟨"
rs = "🟥"

# fmt: off
SYMBOLS = [
    "🍇", "🍈", "🍉",
    "🍊", "🍋", "🍌",
    "🍍", "🥭", "🍎",
    "🍏", "🍐", "🍑",
    "🍒", "🍓", "🫐 ",
    "🥝", "🍅", "🥥",
    "💣", "💀", "❌",
]
# fmt: on

COLOURS: Dict[str, List[str]] = {
    "red": ["🍉", "🍎", "🍒", "🍓", "🍅", "❌"],
    "orange": ["🍊", "🍍", "🥭", "🍑"],
    "yellow": ["🍋", "🍌"],
    "green": ["🍈", "🍏", "🍐", "🥝"],
    "purple": ["🍇", "🫐 ", "💣"],
}

SPECIAL_SYMBOLS = ["💣", "💀", "❌"]
PIRATE_SYMBOLS = ["💀", "❌", "🥥"]


def get_credits() -> int:
    return int(input("Enter credits: "))


def colour_check(s1: str, s2: str, s3: str) -> bool:
    for colour_group in COLOURS.values():
        if s1 in colour_group and s2 in colour_group and s3 in colour_group:
            return True
    return False


def clear() -> None:
    print("\033c", end="")


def print_slots(
    os: str,
    rs: str,
    slot1: str,
    slot2: str,
    slot3: str,
    credits: int,
    jackpot_type: str,
    mult_type: str,
) -> None:
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


def spin_slots() -> List[str]:
    return [random.choice(SYMBOLS) for _ in range(3)]


def format_jackpot(jackpot_message: str, emoji: str) -> str:
    total_width = 20
    message_length = len(jackpot_message)
    spaces_needed = total_width - message_length - 2
    spaces = " " * (spaces_needed // 2)
    return f"{emoji}{spaces}{jackpot_message}{spaces}{emoji}"


def evaluate_spin(
    slot1: str, slot2: str, slot3: str, credits: int
) -> tuple[int, str, str, bool]:
    jackpot_type: str = ""
    mult_type: str = ""
    jackpot: bool = False

    if slot1 == slot2 == slot3 == "💣":
        credits -= math.ceil(credits / 2)
        jackpot_type = format_jackpot("CREDIT BOMB", "🔥")
        mult_type = format_jackpot("÷ 2", "💣")
        jackpot = True
    elif slot1 == slot2 == slot3 == "💀":
        credits -= 667
        jackpot_type = format_jackpot("CREDIT SKULL", "🔥")
        mult_type = format_jackpot("- 667", "💀")
        jackpot = True
    elif slot1 == slot2 == slot3 == "❌":
        credits -= 5000
        jackpot_type = format_jackpot("CREDIT X", "🔥")
        mult_type = format_jackpot("- 5000", "❌")
        jackpot = True
    elif all(s in SPECIAL_SYMBOLS for s in [slot1, slot2, slot3]):
        credits -= 50
        jackpot_type = format_jackpot("OH NO...", "❌")
        mult_type = format_jackpot("- 50", "💣")
        jackpot = True
    elif slot1 == slot2 == slot3:
        credits += 500
        jackpot_type = format_jackpot("CREDIT JACKPOT", "🎰")
        mult_type = format_jackpot("+ 500", "🎰")
        jackpot = True
    elif colour_check(slot1, slot2, slot3):
        credits += 10
        jackpot_type = format_jackpot("COLOUR JACKPOT", "🎰")
        mult_type = format_jackpot("+ 10", "🎰")
        jackpot = True
    elif all(s in PIRATE_SYMBOLS for s in [slot1, slot2, slot3]):
        credits += 250
        jackpot_type = format_jackpot("PIRATE JACKPOT", "🎰")
        mult_type = format_jackpot("+ 250", "🦴")
        jackpot = True
    else:
        jackpot_type = format_jackpot("", rs)
        mult_type = format_jackpot("", rs)
        jackpot = False

    credits -= 1
    return credits, jackpot_type, mult_type, jackpot


def main():
    global os, rs
    credits = get_credits()
    while credits > 0:
        clear()
        slot1, slot2, slot3 = spin_slots()
        credits, jackpot_type, mult_type, jackpot = evaluate_spin(
            slot1, slot2, slot3, credits
        )
        print_slots(os, rs, slot1, slot2, slot3, credits, jackpot_type, mult_type)
        if jackpot:
            time.sleep(3)
        time.sleep(0.35)
        os, rs = rs, os

    print("No credits left :(")
    while True:
        continue


if __name__ == "__main__":
    main()
