# Analyzer class for data analysis
__author__ = "Matteo Golin"

# Imports
import pandas as pd
from customtypes import DateRangeString

# Constants

# Column labels
DATE = "Date"
TRANSACTION_TYPE = "Transaction"
NAME = "Name"
MEMO = "Memo"
AMOUNT = "Amount"


# Class
class Analyzer:

    """Analyzes the transaction data passed through in the processor."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.__load_file()

    def __load_file(self) -> pd.DataFrame:

        """Loads the transactions file and returns a Pandas dataframe containing the file data."""

        return pd.read_csv(self.file_path, index_col=False)

    def search_by_date(self, date: str) -> pd.DataFrame:

        """Returns all transactions made on the given date."""

        return self.data.loc[self.data[DATE] == date]

    def search_by_date_range(self, date_range: DateRangeString) -> pd.DataFrame:

        """Returns all transactions during the given date range."""

        return self.data.loc[self.data[DATE].isin(date_range)]

    def withdrawals(self, date_range: DateRangeString = None) -> pd.DataFrame:

        """Returns all withdrawals, and applies date range if passed."""

        if date_range is not None:
            subset = self.search_by_date_range(date_range)
        else:
            subset = self.data

        return subset.loc[self.data[AMOUNT] < 0]

    def deposits(self, date_range: DateRangeString = None) -> pd.DataFrame:

        """Returns all deposits and applies date range if passed."""

        if date_range is not None:
            subset = self.search_by_date_range(date_range)
        else:
            subset = self.data

        return subset.loc[self.data[AMOUNT] > 0]

    def search_by_transaction_type(self, transaction_type: str, date_range: DateRangeString = None) -> pd.DataFrame:

        """Returns all transactions within the passed date range that match the transaction type."""

        if date_range is not None:
            subset = self.search_by_date_range(date_range)
        else:
            subset = self.data

        return subset.loc[subset[TRANSACTION_TYPE] == transaction_type.upper()]

    def search_by_keyword(self, key_word: str, date_range: DateRangeString = None) -> pd.DataFrame:

        """Returns all transactions within the passed date range that contain the keyword in their memo or name."""

        if date_range is not None:
            subset = self.search_by_date_range(date_range)
        else:
            subset = self.data

        return subset.loc[
            subset[MEMO].str.contains(key_word, case=False) |
            subset[NAME].str.contains(key_word, case=False)
        ]

    def search_by_amount(self, amount: float, tolerance: float = None) -> pd.DataFrame:

        """
        Returns all transactions that have an amount with an absolute value equal to the passed amount.
        The amount can be within the optionally passed tolerance, so that users do not need to remember specific
        amounts.
        """

        if not tolerance:  # Convert NoneType
            tolerance = 0

        lower = amount - tolerance
        upper = amount + tolerance

        return self.data.loc[(lower < abs(self.data[AMOUNT])) & (abs(self.data[AMOUNT]) < upper)]

    def withdrawal_sum(self, date_range: DateRangeString = None) -> float:

        """Returns the sum of the all the withdrawals within the passed date range."""

        subset = self.withdrawals(date_range)

        return round(sum(subset[AMOUNT]), 2)

    def deposit_sum(self, date_range: DateRangeString = None) -> float:

        """Returns the sum of the all the deposits within the passed date range."""

        subset = self.deposits(date_range)

        return round(sum(subset[AMOUNT]), 2)

    def net_amount(self, date_range: DateRangeString = None) -> float:

        """Returns the net sum within the specified date range."""

        withdrawals = self.withdrawal_sum(date_range)
        deposits = self.deposit_sum(date_range)

        return round(withdrawals + deposits, 2)
