import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('BeatlesMusic')


def print_music(music):
    """Print a single movie's details in a readable format.
    song is replaced by music to prevent errors"""
    song = music.get("Song", "Unknown Title")
    year = music.get("Year", "Unknown Year")
    albums = music.get("Album(s)", "No Album(s)")
    length = music.get("Length", "Unknown Length")

    print(f"  Song Name : {song}")
    print(f"  Year Released : {year}")
    print(f"  Album(s): {albums}")
    print(f"  Length: {length} sec")
    print(f"                ")


def print_all_songs():
    """Scan the entire Movies table and print each item."""


    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No songs found. Make sure your DynamoDB table has data.")
        return

    print(f"Found {len(items)} song(s):\n")
    for song in items:
        print_music(song)



def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_songs()


if __name__ == "__main__":
    main()