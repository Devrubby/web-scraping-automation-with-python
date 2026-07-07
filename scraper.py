import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path

HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }

URL_BASE = "https://books.toscrape.com/catalogue/page-{}.html"
ratings_to_number = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def request_page(url_to_scrape):
    """
    Request a page using the requests module, and
     returns the HTML content of the page
    :url_to_scrape: url of the page to request
    :return: HTML content, or None if there are errors
    """
    page_html = None
    try:
        response = requests.get(url_to_scrape, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            page_html = response.text
        else:
            print(f"Error Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return page_html

def parse_page_html(html_text):
    """
    Transform an HTML text, into a Beautifulsoup object and return the object,
    else returns None
    :html_text: The HTML text to transforms
    :return: Beautifulsoup object or None on errors
    """
    soup = BeautifulSoup(html_text, "html.parser")
    if bool(soup.find()):
            return soup
    else:
        return None

def extract_book_data(book_div):
    """
    Extracts details about a book from a Beautifulsoup object.
    Details like [book title, price, rating, etc]
    Returns: A the detailed info extracted as a dictionary
    books_div: The bs4 object to scrape
    """
    book_title = book_div.select_one("h3 > a")
    price = book_div.find("p", class_="price_color")
    rating = book_div.find("p", class_="star-rating")["class"][1].strip()
    availability = book_div.find("p", class_="instock availability").text.strip()
    rating = ratings_to_number.get(rating, 0)
    return {
          "Title": book_title["title"],
          "Price": float(price.string.strip().strip("Â£$€")),
          "Rating": rating,
          "Availability": availability,
          "Product URL": f"https://books.toscrape.com/catalogue/{book_title['href']}"
        }


def scrape_book(max_page=100):
    all_books = []
    for i in range(1, max_page + 1):
        url = URL_BASE.format(i)
        print(f"Currently scraping: {url}")
        page_html = request_page(url)
        if not page_html:
            break
        soup = parse_page_html(page_html)
        if not soup:
            break
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            all_books.append(extract_book_data(book))
    return all_books




def save_json_data(data_to_save, file_name="scraped_books.json"):
    """
     Save json data to a directory, if the file already exists in the directory
    Asks if the file should be overwritten or not
    Data is always saved in the Input_Dir
    :data_to_save: The data to be saved
    :file_name: The file name that the data will be written to
    :return: None
    """
    path = Path("Input_Dir") / file_name
    user_option = "Y"
    if path.is_file():
        user_option = input(f"{file_name} already exist. Enter Y to overwrite or N to exit:").title()
    if user_option == "Y":
        with path.open("w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4)
            print(f"File overwritten and Saved successfully to: {path}")
    else:
        print("File not saved")