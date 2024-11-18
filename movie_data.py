import requests

TMDB_API_KEY = 'your_tmdb_api_key'

def get_poster_url(movie_id):
    """Fetch the poster URL for a movie from TMDb API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

def get_movies_by_ids(movie_ids):
    """Return movie details (poster, title, etc.) for given movie IDs."""
    movie_list = []
    for movie_id in movie_ids:
        movie_data = get_movie_details_from_tmdb(movie_id)
        if movie_data:
            movie_list.append(movie_data)
    return movie_list

def get_movie_details_from_tmdb(movie_id):
    """Fetch movie details from TMDb using the movie_id."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'movieId': movie_id,
            'title': data.get('title'),
            'poster_url': f"https://image.tmdb.org/t/p/w500{data.get('poster_path')}"
        }
    return None
