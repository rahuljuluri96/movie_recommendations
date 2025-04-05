from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Enhanced movie database with 5 languages
movies_db = {
    "english": [
        {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
        {"title": "The Godfather", "genre": "Crime", "rating": 9.2},
        {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
        {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
        {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
        {"title": "Fight Club", "genre": "Drama", "rating": 8.8},
        {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8},
        {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7},
        {"title": "Parasite", "genre": "Thriller", "rating": 8.6},
        {"title": "Whiplash", "genre": "Drama", "rating": 8.5},
        {"title": "Gladiator", "genre": "Action", "rating": 8.5},
        {"title": "Joker", "genre": "Thriller", "rating": 8.4},
        {"title": "The Prestige", "genre": "Mystery", "rating": 8.5},
        {"title": "The Lion King", "genre": "Animation", "rating": 8.5},
        {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4}
    ],
    "hindi": [
        {"title": "3 Idiots", "genre": "Comedy", "rating": 8.4},
        {"title": "Dangal", "genre": "Sports", "rating": 8.4},
        {"title": "Lagaan", "genre": "Sports", "rating": 8.1},
        {"title": "Gangs of Wasseypur", "genre": "Crime", "rating": 8.2},
        {"title": "Andhadhun", "genre": "Thriller", "rating": 8.3},
        {"title": "Taare Zameen Par", "genre": "Drama", "rating": 8.4},
        {"title": "Queen", "genre": "Comedy", "rating": 8.1},
        {"title": "Drishyam", "genre": "Thriller", "rating": 8.2},
        {"title": "Barfi!", "genre": "Romance", "rating": 8.1},
        {"title": "PK", "genre": "Comedy", "rating": 8.1},
        {"title": "Bhaag Milkha Bhaag", "genre": "Sports", "rating": 8.2},
        {"title": "Rang De Basanti", "genre": "Drama", "rating": 8.2},
        {"title": "Dil Chahta Hai", "genre": "Drama", "rating": 8.1},
        {"title": "Swades", "genre": "Drama", "rating": 8.2},
        {"title": "Zindagi Na Milegi Dobara", "genre": "Drama", "rating": 8.1}
    ],
    "tamil": [
        {"title": "Vikram", "genre": "Action", "rating": 8.3},
        {"title": "Ponniyin Selvan", "genre": "Historical", "rating": 7.8},
        {"title": "Jai Bhim", "genre": "Drama", "rating": 8.8},
        {"title": "Super Deluxe", "genre": "Drama", "rating": 8.4},
        {"title": "Kaithi", "genre": "Action", "rating": 8.5},
        {"title": "96", "genre": "Romance", "rating": 8.6},
        {"title": "Anbe Sivam", "genre": "Drama", "rating": 8.6},
        {"title": "Nayakan", "genre": "Crime", "rating": 8.7},
        {"title": "Vada Chennai", "genre": "Crime", "rating": 8.4},
        {"title": "Soodhu Kavvum", "genre": "Comedy", "rating": 8.3},
        {"title": "Pariyerum Perumal", "genre": "Drama", "rating": 8.6},
        {"title": "Aruvi", "genre": "Drama", "rating": 8.5},
        {"title": "Visaranai", "genre": "Crime", "rating": 8.3},
        {"title": "Karnan", "genre": "Drama", "rating": 8.2},
        {"title": "Asuran", "genre": "Action", "rating": 8.3}
    ],
    "telugu": [
        {"title": "Baahubali", "genre": "Action", "rating": 8.1},
        {"title": "RRR", "genre": "Action", "rating": 8.0},
        {"title": "Arjun Reddy", "genre": "Drama", "rating": 7.7},
        {"title": "Pushpa", "genre": "Action", "rating": 7.6},
        {"title": "Eega", "genre": "Fantasy", "rating": 7.9},
        {"title": "Jersey", "genre": "Sports", "rating": 8.3},
        {"title": "C/o Kancharapalem", "genre": "Romance", "rating": 8.6},
        {"title": "Mahanati", "genre": "Biography", "rating": 8.5},
        {"title": "Ala Vaikunthapurramuloo", "genre": "Action", "rating": 7.6},
        {"title": "Rangasthalam", "genre": "Drama", "rating": 8.4},
        {"title": "Bommarillu", "genre": "Romance", "rating": 8.1},
        {"title": "Vedam", "genre": "Drama", "rating": 8.3},
        {"title": "Mathu Vadalara", "genre": "Thriller", "rating": 8.2},
        {"title": "Brochevarevarura", "genre": "Comedy", "rating": 8.4},
        {"title": "Khaleja", "genre": "Action", "rating": 8.1}
    ],
    "malayalam": [
        {"title": "Drishyam", "genre": "Thriller", "rating": 8.6},
        {"title": "Premam", "genre": "Romance", "rating": 8.5},
        {"title": "Bangalore Days", "genre": "Drama", "rating": 8.2},
        {"title": "Kumbalangi Nights", "genre": "Drama", "rating": 8.6},
        {"title": "Maheshinte Prathikaaram", "genre": "Comedy", "rating": 8.4},
        {"title": "Sudani from Nigeria", "genre": "Sports", "rating": 8.3},
        {"title": "Thondimuthalum Driksakshiyum", "genre": "Drama", "rating": 8.3},
        {"title": "Ee.Ma.Yau", "genre": "Drama", "rating": 8.2},
        {"title": "Android Kunjappan", "genre": "Comedy", "rating": 8.0},
        {"title": "Ustad Hotel", "genre": "Drama", "rating": 8.3},
        {"title": "Joji", "genre": "Crime", "rating": 8.1},
        {"title": "The Great Indian Kitchen", "genre": "Drama", "rating": 8.8},
        {"title": "Jallikattu", "genre": "Thriller", "rating": 7.9},
        {"title": "Lucifer", "genre": "Action", "rating": 7.8},
        {"title": "Minnal Murali", "genre": "Superhero", "rating": 7.9}
    ]
}

# Map genres to all available movies with that genre
genres_map = {}
for language, movies in movies_db.items():
    for movie in movies:
        genre = movie["genre"]
        if genre not in genres_map:
            genres_map[genre] = []
        movie_with_language = movie.copy()
        movie_with_language["language"] = language
        genres_map[genre].append(movie_with_language)

@app.route('/')
def index():
    all_genres = sorted(set(genres_map.keys()))
    all_languages = sorted(movies_db.keys())
    return render_template('index.html', genres=all_genres, languages=all_languages)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    selected_genres = request.form.getlist('genres')
    selected_languages = request.form.getlist('languages')
    min_rating = float(request.form.get('rating', 0))
    
    if not selected_genres:
        selected_genres = list(genres_map.keys())
    if not selected_languages:
        selected_languages = list(movies_db.keys())
    
    recommendations = []
    for genre in selected_genres:
        if genre in genres_map:
            for movie in genres_map[genre]:
                if movie["language"] in selected_languages and movie["rating"] >= min_rating:
                    recommendations.append({
                        "title": movie["title"],
                        "genre": movie["genre"],
                        "language": movie["language"].capitalize(),
                        "rating": movie["rating"]
                    })
    
    if recommendations:
        random.shuffle(recommendations)
        recommendations = sorted(recommendations, key=lambda x: x['rating'], reverse=True)[:10]
    
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)