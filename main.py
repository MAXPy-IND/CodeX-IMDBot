import imdb

# Create an instance of the IMDb class
ia = imdb.IMDb()

def get_movie_info(movie_title):
    try:
        # Search for movies that match the title
        movies = ia.search_movie(movie_title)

        if not movies:
            return "No movie found with that title."

        # Get the first movie's details
        movie = movies[0]
        ia.update(movie)
        title = movie.get("title", "N/A")
        year = movie.get("year", "N/A")
        rating = movie.get("rating", "N/A")
        plot = movie.get("plot", "N/A")
        genres = ", ".join(movie.get("genres", ["N/A"]))

        result = (
            f"Title: {title}\nYear: {year}\nRating: {rating}\nGenres: {genres}\nPlot: {plot}"
        )
        return result
    except Exception as e:
        return str(e)

def imdb_chatbot():
    print("IMDb Chat Bot")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = get_movie_info(user_input)
        print(f"Bot: {result}")

if __name__ == "__main__":
    imdb_chatbot()
