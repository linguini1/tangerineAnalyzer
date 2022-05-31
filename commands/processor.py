# Processor object for running logic with passed commandline commands
__author__ = "Matteo Golin"

# Imports
from customtypes import DateRangeString
from analysis.analyzer import Analyzer
import analysis.dates as dates

# Constants
SUBCOMMAND_ID = "subcommand"
TIME_PERIODS = ["days", "weeks", "months", "year"]


# Class
class CommandProcessor:

    """Decide what logic to execute given the commandline arguments."""

    def __init__(self, arguments: dict):
        self.arguments = arguments

        print(arguments)  # DEBUG ONLY

        # Unpacking important arguments
        self.subcommand = self.arguments.get(SUBCOMMAND_ID)
        self.transaction_file = self.arguments.get("transaction file")

        # Initialize analyzer
        self.analyzer = Analyzer(self.transaction_file)

        # Get a specified date range
        self.date_range = self.__process_date_range()

    def __process_date_range(self) -> DateRangeString | str | None:

        """Returns the specified date range."""

        # See which period of time the user specified
        specified_period = None
        for period in TIME_PERIODS:
            if self.arguments.get(period) is not None:
                specified_period = period
                break

        value = self.arguments.get(specified_period)  # Value of the specified period (# of days, months, etc.)

        # Return the matching date range
        match specified_period:
            case "days":
                return dates.past_days(days=value)
            case "weeks":
                return dates.past_weeks(weeks=value)
            case "months":
                return dates.past_months(months=value)
            case "year":
                return dates.past_year()
            case None:
                return None

    def run_logic(self):

        """Runs the required logic based on the given subcommand."""

        match self.subcommand:

            case "date-search":
                if type(self.date_range) is list:
                    return self.analyzer.search_by_date_range(self.date_range)
                else:
                    return self.analyzer.search_by_date(self.date_range)

            case "withdrawals":
                if self.arguments.get("sum"):
                    return self.analyzer.withdrawal_sum(self.date_range)
                return self.analyzer.withdrawals(self.date_range)

            case "deposits":
                if self.arguments.get("sum"):
                    return self.analyzer.deposit_sum(self.date_range)
                return self.analyzer.deposits(self.date_range)

            case "balance":
                return self.analyzer.net_amount(self.date_range)

            case "transaction-type":
                transaction_type = self.arguments.get("type")
                return self.analyzer.search_by_transaction_type(transaction_type, self.date_range)

            case "keyword-search":
                key_word = self.arguments.get("keyword")
                return self.analyzer.search_by_keyword(key_word, self.date_range)

            case "amount-search":
                amount = self.arguments.get("amount")
                tolerance = self.arguments.get("tolerance")
                return self.analyzer.search_by_amount(amount, tolerance)
