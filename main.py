import random
import time
import math
from typing import List, Dict


class SlotMachine:
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

    def __init__(self, credits: int):
        self.os = "🟨"
        self.rs = "🟥"
        self.credits = credits
        self.slot1: str = ""
        self.slot2: str = ""
        self.slot3: str = ""
        self.jackpot_type: str = ""
        self.mult_type: str = ""
        self.jackpot: bool = False

    def colour_check(self, s1: str, s2: str, s3: str) -> bool:
        for colour_group in self.COLOURS.values():
            if s1 in colour_group and s2 in colour_group and s3 in colour_group:
                return True
        return False

    def clear(self) -> None:
        print("\033c", end="")

    def print_slots(self) -> None:
        credit_str = str(self.credits)
        total_width = 18
        pad = total_width - len(credit_str)
        left = pad // 2
        right = pad - left
        spaces_left = " " * left
        spaces_right = " " * right

        print(
            f"{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}{self.rs}{self.os}"
        )
        print(f"{self.jackpot_type}")
        print(f"{self.os}     {self.slot1} {self.slot2} {self.slot3}     {self.os}")
        print(f"{self.mult_type}")
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

    def evaluate_spin(self) -> tuple[int, str, str, bool]:
        self.jackpot_type: str = ""
        self.mult_type: str = ""
        self.jackpot: bool = False

        match (self.slot1, self.slot2, self.slot3):
            case ("💣", "💣", "💣"):
                self.credits -= math.ceil(self.credits / 2)
                self.jackpot_type = self.format_jackpot("CREDIT BOMB", "🔥")
                self.mult_type = self.format_jackpot("÷ 2", "💣")
                self.jackpot = True
            case ("💀", "💀", "💀"):
                self.credits -= 667
                self.jackpot_type = self.format_jackpot("CREDIT SKULL", "🔥")
                self.mult_type = self.format_jackpot("- 667", "💀")
                self.jackpot = True
            case ("❌", "❌", "❌"):
                self.credits -= 5000
                self.jackpot_type = self.format_jackpot("CREDIT X", "🔥")
                self.mult_type = self.format_jackpot("- 5000", "❌")
                self.jackpot = True
            case _ if all(
                s in self.SPECIAL_SYMBOLS for s in [self.slot1, self.slot2, self.slot3]
            ):
                self.credits -= 50
                self.jackpot_type = self.format_jackpot("OH NO...", "❌")
                self.mult_type = self.format_jackpot("- 50", "💣")
                self.jackpot = True
            case _ if self.slot1 == self.slot2 == self.slot3:
                self.credits += 500
                self.jackpot_type = self.format_jackpot("CREDIT JACKPOT", "🎰")
                self.mult_type = self.format_jackpot("+ 500", "🎰")
                self.jackpot = True
            case _ if self.colour_check(self.slot1, self.slot2, self.slot3):
                self.credits += 10
                self.jackpot_type = self.format_jackpot("COLOUR JACKPOT", "🎰")
                self.mult_type = self.format_jackpot("+ 10", "🎰")
                self.jackpot = True
            case _ if all(
                s in self.PIRATE_SYMBOLS for s in [self.slot1, self.slot2, self.slot3]
            ):
                self.credits += 250
                self.jackpot_type = self.format_jackpot("PIRATE JACKPOT", "🎰")
                self.mult_type = self.format_jackpot("+ 250", "🦴")
                self.jackpot = True
            case _:
                self.jackpot_type = self.format_jackpot("", self.rs)
                self.mult_type = self.format_jackpot("", self.rs)
                self.jackpot = False

        self.credits -= 1
        return self.credits, self.jackpot_type, self.mult_type, self.jackpot

    def play(self):
        while self.credits > 0:
            self.clear()
            self.slot1, self.slot2, self.slot3 = self.spin_slots()
            self.evaluate_spin()
            self.print_slots()
            if self.jackpot:
                time.sleep(3)
            time.sleep(0.35)
            self.os, self.rs = self.rs, self.os

        print("No credits left :(")
        while True:
            continue


def get_credits() -> int:
    try:
        credits = int(input("Enter credits: "))
        if credits < 1:
            raise ValueError
        return credits
    except ValueError:
        print("Please enter a valid positive integer.")
        return get_credits()


if __name__ == "__main__":
    credits = get_credits()
    game = SlotMachine(credits)
    game.play()
