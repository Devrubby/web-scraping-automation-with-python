from scraper import  scrape_book, save_json_data
from analysis import make_stats, rating_distribution, load_books_df
from pathlib import Path
from excel_report import build_excel_report


output_path = Path("Output_Dir")
def main():
    try:
        data = scrape_book()
        save_json_data(data)
    except Exception as e:
        print(f"Scraping failed: {e}")
        return
    try:
        input_path = Path("Input_Dir/scraped_books.json")
        books_details = load_books_df(input_path)
        books_stats = make_stats(books_details)
        ratings_spread = rating_distribution(books_details)
    except FileNotFoundError:
        print("Input JSON file not found")
        return
    build_excel_report(books_details, books_stats, ratings_spread, output_path=output_path)


if __name__ == "__main__":
     main()