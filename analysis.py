import pandas as pd


def load_books_df(file_path):
    return pd.read_json(file_path)


def make_stats(df):
    stats_summary = {
        "Total books scraped": df.shape[0],
        "Average price": round(float(df["Price"].mean()), 2),
        "Highest price": float(df["Price"].max()),
        "Lowest price": float(df["Price"].min()),
        "Average rating": round(float(df["Rating"].mean()), 1),
        "Total available books": int(df["Availability"].str.contains("In stock").sum()),
        "Total unavailable books": (~df["Availability"].str.contains("In stock")).sum()
    }
    return  stats_summary

def rating_distribution(df):
    ratings_count = df["Rating"].value_counts().sort_index()
    ratings_count.index.name = None
    return {key: int(val) for key, val in dict(ratings_count).items()}