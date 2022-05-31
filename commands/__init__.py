# Commandline commands
__author__ = "Matteo Golin"

# Imports
import argparse
from .validators import PositiveNumber, CSVFile
from .processor import SUBCOMMAND_ID

# Constants
HELP_STATEMENTS = {
    "parser": "Command line tool for analyzing and sorting through Tangerine transactions in csv file format.",
    "subparsers": "A list of subcommands that can be used to sort, search and analyze transactions.",
}


# Parser
class CustomParser(argparse.ArgumentParser):

    def error(self, message: str) -> None:
        if "the following arguments are required: transaction file" in message:
            pass
        else:
            super(CustomParser, self).error(message)


parser = CustomParser(description=HELP_STATEMENTS["parser"])
subparsers = parser.add_subparsers(help=HELP_STATEMENTS["subparsers"], dest=SUBCOMMAND_ID)

# Transaction filepath
parser.add_argument(
    "transaction file",
    type=CSVFile,
    help="Full file path to the CSV file containing Tangerine transaction information.",
)

# Date range handling
date_range = parser.add_mutually_exclusive_group()
date_range.add_argument(
    "-days", "-d",
    help="Specifies how many days in the past to search.",
    type=PositiveNumber,
)

date_range.add_argument(
    "-weeks", "-w",
    help="Specifies how many weeks in the past to search.",
    type=PositiveNumber,
)

date_range.add_argument(
    "-months", "-m",
    help="Specifies how many months in the past to search.",
    type=PositiveNumber,
)

date_range.add_argument(
    "-year", "-y",
    help="Specifies a date range of 1 year for the search.",
    action="store_true"
)

# TODO add custom date range

# Subcommands
date_search = subparsers.add_parser(
    "date-search",
    help="Search for transactions with a date range."
)

withdrawals = subparsers.add_parser(
    "withdrawals",
    help="Search withdrawals."
)

withdrawals.add_argument(
    "-sum", "-s",
    action="store_true",
    help="Returns the sum of all the withdrawals within the date range."
)

deposits = subparsers.add_parser(
    "deposits",
    help="Search deposits."
)

deposits.add_argument(
    "-sum", "-s",
    action="store_true",
    help="Returns the sum of all the deposits within the date range."
)

net_total = subparsers.add_parser(
    "balance",
    help="Get the balance of the account within the date range."
)

transaction_type = subparsers.add_parser(
    "transaction-type",
    help="Search transactions based on the transaction type."
)

transaction_type.add_argument(
    "type",
    metavar="TRANSACTION-TYPE",
    choices=["other", "pos", "credit"],
    help="Transaction type to search for."
)

key_word_search = subparsers.add_parser(
    "keyword-search",
    help="Search for transactions using a keyword."
)

key_word_search.add_argument(
    "keyword",
    metavar="WORD",
    type=str,
    help="Keyword to search for."
)

amount_search = subparsers.add_parser(
    "amount-search",
    help="Search transactions based on estimated amount."
)

amount_search.add_argument(
    "amount",
    type=PositiveNumber,
    metavar="AMOUNT",
    help="Amount to search for."
)

amount_search.add_argument(
    "-tolerance", "-t",
    type=PositiveNumber,
    metavar="TOL",
    help="Provides a tolerance for the passed amount within which searches will be valid."
)

