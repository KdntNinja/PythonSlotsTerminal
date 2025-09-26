
# Color groups for checking matches
COLORS: Dict[str, List[str]] = {
    "red": ["🍉", "🍎", "🍒", "🍓", "🍅", "❌"],
    "orange": ["🍊", "🍍", "🥭", "🍑"],
    "yellow": ["🍋", "🍌"],
    "green": ["🍈", "🍏", "🍐", "🥝"],
    "purple": ["🍇", "🫐", "💣"]
}

def colour_check(s1: str, s2: str, s3: str) -> bool:
    for color_group in COLORS.values():
        if s1 in color_group and s2 in color_group and s3 in color_group:
            return True
    return False