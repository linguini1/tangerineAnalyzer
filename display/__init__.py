# Functions for display
__author__ = "Matteo Golin"

# Imports
import pandas as pd

# Settings
pd.set_option("display.max_rows", None)  # All results are printed


# Functions
def print_results(results) -> None:

    """Prints the results appropriately based on their value."""

    if type(results) == pd.DataFrame:
        print(results.to_string(index=False))
    elif type(results) == float:
        print(f"Amount: ${results}")
