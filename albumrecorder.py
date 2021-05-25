##
# album_recommender.py
# Rhiannon MacCreadie
# Class code practice assessment
# Asks user to enter an album
# Album contains title,artist, genre, rating
# User can add, edit, delete, and rate albums
# If the user rates album it should recommend another one

def add(albums):
    """
Adds an album, to the albums collection
Asks user for title, artist, genre, and rating
Returns the updated album
    """
    # Add title, artist, and genre which are strings
    title = input("Title: ")
    artist = input("Artist: ")
    genre = input("Genre: ")

    # Add a rating between 1 to 5 and forces input
    MIN_RATING = 1
    MAX_RATING = 5
    while True:
        try:
            rating = int(input("Rating out of {}: ".format(MAX_RATING)))
            if rating < MIN_RATING or rating > MAX_RATING:
                print("Rating must be between {}-{}".format(MIN_RATING,MAX_RATING))
            else:
                break
        except ValueError:
            print("Rating must be between {}-{}".format(MIN_RATING,MAX_RATING))
    # Add the vakues to the album dictionary
    album = {"title":title, "artist":artist, "genre":genre, "rating":rating}

    # Add our album to our albums collection

# Edit Function


# Delete Function


# Display Function


# Rate Function


# Recommend Function


# Menu
def menu(albums, album_id):
    """
Displays the option to the user and calls accordingly.
    """

    # Prints the menu and loops until user quits
    while True:
        print("""
Welcome to Album rater and recommender
(A)dd a album
(E)dit an album
(D)elete an album
(P)rint all albums
(R)ate an album
(Q)uit """)
        choice = input("Please enter your option... ").upper()

        # Calls the users options
        if 
              

return albums, album_id
# Main Routine
if __name__ == "__main__":
    # declearing a  dictionary of  album dictionaries
    albums = {}

    # track current album ID
    album_id = 0
    menu(albums, album_id)
    
    
