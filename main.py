import random
import time
import math
from typing import List, Dict


class PythonSlotsTerminal:
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

    def __init__(self):
        self.os = "🟨"
        self.rs = "🟥"
        self.credits = 0

    def get_credits(self) -> int:
        return int(input("Enter credits: "))

    @classmethod
    def colour_check(cls, s1: str, s2: str, s3: str) -> bool:
        for colour_group in cls.COLOURS.values():
            if s1 in colour_group and s2 in colour_group and s3 in colour_group:
                return True
        return False

    @staticmethod
    def clear() -> None:
        print("\033c", end="")

    def print_slots(
        self,
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

        print(
            f"{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}"
        )
        print(f"{jackpot_type}")
        print(f"{self.os}     {slot1} {slot2} {slot3}     {self.os}")
        print(f"{mult_type}")
        print(
            f"{self.os}     Credits:     {self.os}\n{self.rs}{spaces_left}{credit_str}{spaces_right}{self.rs}\n{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}"
        )

    def spin_slots(self) -> List[str]:
        return [random.choice(self.SYMBOLS) for _ in range(3)]

    @staticmethod
    def format_jackpot(jackpot_message: str, emoji: str) -> str:
        total_width = 20
        message_length = len(jackpot_message)
        spaces_needed = total_width - message_length - 2
        spaces = " " * (spaces_needed // 2)
        return f"{emoji}{spaces}{jackpot_message}{spaces}{emoji}"

    def evaluate_spin(
        self, slot1: str, slot2: str, slot3: str, credits: int
    ) -> tuple[int, str, str, bool]:
        jackpot_type: str = ""
        mult_type: str = ""
        jackpot: bool = False

        match (slot1, slot2, slot3):
            case ("💣", "💣", "💣"):
                credits -= math.ceil(credits / 2)
                jackpot_type = self.format_jackpot("CREDIT BOMB", "🔥")
                mult_type = self.format_jackpot("÷ 2", "💣")
                jackpot = True
            case ("💀", "💀", "💀"):
                credits -= 667
                jackpot_type = self.format_jackpot("CREDIT SKULL", "🔥")
                mult_type = self.format_jackpot("- 667", "💀")
                jackpot = True
            case ("❌", "❌", "❌"):
                credits -= 5000
                jackpot_type = self.format_jackpot("CREDIT X", "🔥")
                mult_type = self.format_jackpot("- 5000", "❌")
                jackpot = True
            case _ if all(s in self.SPECIAL_SYMBOLS for s in [slot1, slot2, slot3]):
                credits -= 50
                jackpot_type = self.format_jackpot("OH NO...", "❌")
                mult_type = self.format_jackpot("- 50", "💣")
                jackpot = True
            case _ if slot1 == slot2 == slot3:
                credits += 500
                jackpot_type = self.format_jackpot("CREDIT JACKPOT", "🎰")
                mult_type = self.format_jackpot("+ 500", "🎰")
                jackpot = True
            case _ if self.colour_check(slot1, slot2, slot3):
                credits += 10
                jackpot_type = self.format_jackpot("COLOUR JACKPOT", "🎰")
                mult_type = self.format_jackpot("+ 10", "🎰")
                jackpot = True
            case _ if all(s in self.PIRATE_SYMBOLS for s in [slot1, slot2, slot3]):
                credits += 250
                jackpot_type = self.format_jackpot("PIRATE JACKPOT", "🎰")
                mult_type = self.format_jackpot("+ 250", "🦴")
                jackpot = True
            case _:
                jackpot_type = self.format_jackpot("", self.rs)
                mult_type = self.format_jackpot("", self.rs)
                jackpot = False

        credits -= 1
        return credits, jackpot_type, mult_type, jackpot

    def run(self):
        self.credits = self.get_credits()
        while self.credits > 0:
            self.clear()
            slot1, slot2, slot3 = self.spin_slots()
            self.credits, jackpot_type, mult_type, jackpot = self.evaluate_spin(
                slot1, slot2, slot3, self.credits
            )
            self.print_slots(slot1, slot2, slot3, self.credits, jackpot_type, mult_type)
            if jackpot:
                time.sleep(3)
            time.sleep(0.35)
            self.os, self.rs = self.rs, self.os

        print("No credits left :(")
        while True:
            continue


if __name__ == "__main__":
    PythonSlotsTerminal().run()
