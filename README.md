Web Scraping Automation with Python

Overview

This project demonstrates a complete Python web scraping and reporting workflow using the practice website Books to Scrape. It sends HTTP requests to retrieve book data, parses HTML using Beautiful Soup, follows pagination to scrape multiple pages, processes the extracted information, and generates a professionally formatted Excel report containing summary statistics and rating distributions.

Technologies Used

- Python
- requests
- Beautiful Soup (bs4)
- pandas
- openpyxl
- pathlib
- json

Features

- Scrapes book data from multiple pages automatically
- Extracts book title, price, rating, availability, and product URL
- Handles website pagination
- Saves the scraped data as a JSON file
- Analyzes the scraped data using pandas
- Calculates summary statistics, including:
  - Total books scraped
  - Average book price
  - Highest and lowest book prices
  - Average book rating
  - Number of available and unavailable books
  - Rating distribution
- Generates a formatted multi-sheet Excel report containing:
  - Book Details
  - Summary Statistics
  - Rating Distribution
- Automatically adjusts Excel column widths and applies basic formatting

Project Structure

scraper.py          # Scrapes book data and saves JSON
analysis.py         # Performs data analysis with pandas
excel_report.py     # Generates the Excel report
main.py             # Coordinates the entire workflow
Input_Dir/          # Stores the input data
Output_Dir/         
README.md

How to Run

1. Clone the repository.
2. Install the required packages.
3. Run "main.py".
4. The program will scrape the website, save the JSON data, analyze the dataset, and generate an Excel report in the "Output_Dir" folder.