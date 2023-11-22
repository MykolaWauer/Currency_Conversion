## Currency_Conversion

Currency Conversion Script with pandas and forex-python

## Overview

This Python script performs currency conversion on an Excel file containing sales data. 
It utilizes the powerful data manipulation library, pandas, to handle Excel data and the forex-python library to fetch daily updated exchange rates. 
The converted data is then saved to a new Excel file using openpyxl.

## Features

- Converts currency values from Krone (CZK) to Euro (EUR) based on daily exchange rates
- Uses pandas for efficient data manipulation
- Retrieves exchange rates from forex-python
- Saves the results to a new Excel file with openpyxl

## Requirements

- Python 3.x
- pandas==<2.1.3>
- forex-python==<1.6>
- openpyxl==<3.1.2>

## Usage

1. Install the required packages: `pip install -r requirements.txt`
2. Run the script: `python currency_conversion_script.py`
