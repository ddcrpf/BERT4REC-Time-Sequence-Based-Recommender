from flask import Flask, render_template, request, jsonify
import model  # Your model for predictions
import movie_data  # TMDb integration for fetching movie data

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch a list of movies (initial set for user to select)
    movies = movie_data.get_all_movies()  # Pre-selected movie list from TMDb
    return render_template('index.html', movies=movies)

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get movie IDs from the front-end (selected posters)
    selected_movie_ids = request.json['selected_movie_ids']
    
    # Call the prediction model
    recommended_movie_ids = model.predict_recommendations(selected_movie_ids, num_recommendations=10)
    
    # Get poster URLs for the recommended movie IDs
    recommended_movies = movie_data.get_movies_by_ids(recommended_movie_ids)
    
    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
