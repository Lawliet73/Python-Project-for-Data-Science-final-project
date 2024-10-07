# Tesla and GameStop Stock and Revenue Data Analysis

This project retrieves and analyzes historical stock and revenue data for Tesla (TSLA) and GameStop (GME) using Python. The project uses data from Yahoo Finance via the `yfinance` library for stock prices and web scraping techniques using `pandas` to gather revenue data from a publicly available website. This analysis is displayed via interactive plots using Plotly.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Author](#author)

## Project Overview
This project performs the following tasks:
- Fetches historical stock price data for Tesla (TSLA) using the `yfinance` library.
- Scrapes Tesla's quarterly revenue data using the `pandas` `read_html()` method.
- Processes and cleans the scraped data by removing unwanted characters and handling missing values.
- Plots both the stock price and revenue data on interactive graphs using Plotly for visual analysis.

A similar script can be used for GameStop (GME) by following the same approach.

## Requirements
To run this project, you will need the following Python libraries:
- `pandas`
- `yfinance`
- `plotly`
- `urllib`

You can install the required libraries using the following command:


pip install pandas yfinance plotly

## Setup Instructions

### Clone the repository:

git clone https://github.com/yourusername/stock-revenue-analysis.git
cd stock-revenue-analysis
Install dependencies:
Make sure you have Python installed and run the following command to install the necessary packages:


pip install -r requirements.txt
Run the script:
Run the Python script to retrieve, clean, and plot the stock and revenue data:


## Usage
The script retrieves historical stock price data for Tesla using yfinance.
It then scrapes quarterly revenue data from a given URL.
After cleaning and processing the revenue data (removing dollar signs, commas, and handling missing values), it plots both the stock price and revenue data on an interactive graph using Plotly.
To plot data for a different stock, you can modify the Ticker symbol and revenue URL accordingly.



## Code Explanation
- Retrieving Tesla Stock Data:
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

- Scraping Revenue Data:
The script uses pandas.read_html() to scrape the revenue data from the specified URL. The second table on the page is selected, and the column names are renamed for clarity.

- Data Cleaning:
The revenue column is cleaned by removing commas and dollar signs, and rows with missing or empty values are dropped.
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r',|\$',"", regex=True)
tesla_revenue.dropna(inplace=True)

- Plotting Data:
The make_graph function generates a two-row subplot: one for stock prices and one for revenue data.
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=.3)


## Author
Kalab Alemayehu


