<p align="center">
<img style="width:100px; height:100px;" src="IMDb Logo.png" alt="Pirogram-IMDBot Logo">
</p>

<h1 align="center">
<a href="https://github.com/MAXPy-IND/Pirogram-IMDBot">Pirogram IMDBot</a>
</h1>

<p align="center">
    <img src="https://img.shields.io/github/license/MAXPy-IND/Pirogram-IMDBot?style=for-the-badge&logo=appveyor" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/MAXPy-IND/Pirogram-IMDBot?style=for-the-badge&logo=appveyor" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/MAXPy-IND/Pirogram-IMDBot?style=for-the-badge&logo=appveyor" alt="Repository Size"> <br>
    <img src="https://img.shields.io/github/issues/MAXPy-IND/Pirogram-IMDBot?style=for-the-badge&logo=appveyor" alt="Issues">
    <img src="https://img.shields.io/github/forks/MAXPy-IND/Pirogram-IMDBot?style=for-the-badge&logo=appveyor" alt="Forks">
    <img src="https://img.shields.io/github/stars/MAXPy-IND/Pirogram-IMDBot?style=for-the-badge&logo=appveyor" alt="Stars">
</p>

A Chat Bot written in python for search movie details like IMDb..!!


### Credits

- Thanks to - [God..!](https://en.wikipedia.org/wiki/God)
- Thanks to - [Python..!](www.python.org)
- Thanks to - [IMDb..!](http://www.imdb.com/)
- Thanks to - [Requests..!](https://requests.readthedocs.io/0)
- Thanks to - [ME..!](https://github.com/MAXPy-IND)
- Thanks to - [Pirogram..!](https://tt.me/maxpy)


### Deployment

<details><summary>Tutorial Video</summary>
<p>
<br>
alt="Pirogram-IMDBot Logo">
</p>
</details>

- [x] Code

```
import requests

OMDB_API_KEY = 'f04cefcb'

def get_movie_info(movie_title):
    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "False":
            return "No movie found with that title."

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

def pirogram():
    print("""Welcome to Pirogram IMDBot, You can get details about a movie through this Chat Bot..!!""")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = get_movie_info(user_input)
        print(f"Bot: {result}")

if __name__ == "__main__":
    pirogram()
```    


