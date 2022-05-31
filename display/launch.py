# Launch screen display
__author__ = "Matteo Golin"

# Constants
TANGERINE_LOGO = "display/tangerine.txt"  # Relative from main file
HELP_REMINDER = "To learn how to use the command line tool, in your console type:\n" \
                "py main.py -h"
RED_CODE = "\033[91m"  # Turns text red


# Functions
def get_logo() -> str:

    """Returns the Tangerine logo as a string."""

    logo = ""
    with open(TANGERINE_LOGO, "r") as file:
        for line in file:
            logo += line
    return logo


def launch_screen():
    print(get_logo())
    print("tangerineAnalyzer by Matteo Golin")
    print(f"https://github.com/linguini1/tangerineAnalyzer{RED_CODE}\n")
    print(HELP_REMINDER)
    quit()
