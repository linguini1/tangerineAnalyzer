# Validators for command line arguments
__author__ = "Matteo Golin"

# Imports
import os


# Types
def PositiveNumber(num: str) -> int | float:

    """Ensures that the passed number is positive."""

    try:
        num = float(num)
    except ValueError:
        raise ValueError("Argument is not a number.")

    if num <= 0:
        raise ValueError("Number must be a positive value.")

    return num


def CSVFile(file_path: str) -> str:

    """Checks to see if the passed file is a valid CSV file."""

    relative_path = f"{os.getcwd()}\\{file_path}"

    if ".csv" not in file_path:
        raise TypeError("File is not a CSV file.")

    if not os.path.isfile(file_path) and not os.path.isfile(relative_path):
        raise FileNotFoundError("The file does not exist.")

    return relative_path if os.path.isfile(relative_path) else file_path
