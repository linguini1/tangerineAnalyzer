# Transaction analyzer for tangerine transactions
__author__ = "Matteo Golin"

# Imports
from commands import parser
from commands.processor import CommandProcessor
from display import print_results
from display.launch import launch_screen

# Main
if __name__ == "__main__":
    arguments = vars(parser.parse_args())  # Unpack arguments

    # If the program is run with no arguments, run intro screen
    if not any(arguments.values()):
        launch_screen()

    # Continue with logic
    processor = CommandProcessor(arguments)
    results = processor.run_logic()  # Process
    print_results(results)  # Display
