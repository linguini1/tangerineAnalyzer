# tangerineAnalyzer
### Matteo Golin

Functions as a command line tool for analyzing and searching transactions from Tangerine banking. Files must be in CSV
format.

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](https://opensource.org/licenses/MIT)

## Usage
To see full usage of the commandline options, please type `py main.py -h` in the console.

All commands are indicated by a subcommand, such as searching by `amount-search` or by `keyword-search`. All commands 
require a path to the transactions CSV file, and take an optional date range to search within.

Note that if no date range is specified, the software will search all transactions. This means that it is valid to run
`date-search` without a specified date range, however it is equivalent to showing all transactions.

## Display
If the program is run with no commandline arguments, a launch screen is shown with an indication on how to view the help
for the CLI.

Results are printed immediately after execution. Transactions lists are printed with the formatting done by the pandas
module, and all numerical results are printed in plain text with a `Amount: $<number>` indicator.

## Installation
This program requires the following dependencies:
- Pandas
- Python 3.10.0 or later
The program also requires a valid CSV file to run. The CSV file must be in the same format as the transaction details
CSV provided by Tangerine Bank.

## Features in Development
- Custom date ranges
- Single date search