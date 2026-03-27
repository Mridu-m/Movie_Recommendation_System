import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    movies = pd.read_csv('data/tmdb_5000_movies.csv')
    credits = pd.read_csv('data/tmdb_5000_credits.csv')
    return movies.merge(credits, on='title')


def preprocess(movies):
    movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
    movies.dropna(inplace=True)

    def convert(text):
        L = []
        for i in ast.literal_eval(text):
            L.append(i['name'])
        return L

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)

    movies['tags'] = movies['overview'] + movies['genres'].astype(str)
    movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

    return movies


def create_similarity(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    return cosine_similarity(vectors)


def recommend(movie, movies, similarity):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]
