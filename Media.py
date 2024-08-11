from flask import Flask, render_template

app = Flask(__name__)

# Sample data: A list of dictionaries representing movies/TV shows
media_list = [
    {"title": "Breaking Bad", "type": "TV Show", "description": "A high school chemistry teacher turned methamphetamine producer."},
    {"title": "Inception", "type": "Movie", "description": "A thief who steals corporate secrets through the use of dream-sharing technology."},
    {"title": "The Matrix", "type": "Movie", "description": "A computer hacker learns about the true nature of reality and his role in the war against its controllers."},
    {"title": "Stranger Things", "type": "TV Show", "description": "A group of kids uncovering government secrets and facing supernatural forces in their town."},
]

@app.route('/')
def index():
    return render_template('index.html', media_list=media_list)

if __name__ == '__main__':
    app.run(debug=True)
