import requests

OMDB_API_KEY = 'f04cefcb'

def get_movie_info(movie_title):
    try:
        # Create a request to the OMDB API
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "False":
            return "No movie found with that title."

        # Extract movie details from the API response
        title = data.get("Title", "N/A")
        year = data.get("Year", "N/A")
        rating = data.get("imdbRating", "N/A")
        genres = data.get("Genre", "N/A")
        plot = data.get("Plot", "N/A")

        result = (
            f"Title: {title}\nYear: {year}\nRating: {rating}\nGenres: {genres}\nPlot: {plot}"
        )
        return result
    except Exception as e:
        return str(e)

def max():
    print("""Welcome to MAX IMDBot, You can get details about a movie through this Chat Bot..!!")
    print("Type exit to quit")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = get_movie_info(user_input)
        print(f"Bot: {result}")

if __name__ == "__main__":
    max()

