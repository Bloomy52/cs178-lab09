# read_movies.py
# Reads all items from the DynamoDB Movies table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Movies"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_movie(movie):
    """Print a single movie's details in a readable format."""
    title = movie.get("Title", "Unknown Title")
    year = movie.get("Year", "Unknown Year")
    ratings = movie.get("Ratings", "No ratings")
    genres = movie.get("Genre", "No genres")
    runtime = movie.get("Runtime (min)", "Unknown Runtime")
    
    # Ratings is a nested map in the table — handle it gracefully
    #ratings = movie.get("Ratings", {})
    #rating_str = ", ".join(f"{k}: {v}" for k, v in ratings.items()) if ratings else "No ratings"
    
    print(f"  Title : {title}")
    print(f"  Year  : {year}")
    print(f"  Ratings: {ratings}")
    print(f"  Genres: {genres}")
    print(f"  Runtime: {runtime} min")
    print(f"                ")


def print_all_movies():
    """Scan the entire Movies table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No movies found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} movie(s):\n")
    for movie in items:
        print_movie(movie)


def get_movie_by_title():
    title = input("Please enter a movie title: ")
    table = get_table()


    response = table.scan(
        FilterExpression=Key("Title").eq(title)
    )
    items = response.get("Items", [])

    if not items:
        print(f"Movie not found:")
        return

    for movie in items:
        print_movie(movie)




def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_movies()
    get_movie_by_title()


if __name__ == "__main__":
    main()
