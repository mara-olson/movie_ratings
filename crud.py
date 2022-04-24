"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def return_all_users():
    """Return all movies."""
    return User.query.all()

def get_user_by_id(user_id): 
    """Return user detail with a given id"""
    return User.query.get(user_id)

def get_user_by_email(email): 
    """Return user detail with a given email"""
    return User.query.filter(User.email == email).first()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,
    )

    return movie

def return_all_movies():
    """Return all movies."""
    return Movie.query.all()

def get_movie_by_id(movie_id): 
    """"Return title of movie with a given id"""
    return Movie.query.get(movie_id)

def get_movie_by_title(title): 
    """"Return movie object from a given id"""
    return Movie.query.filter(Movie.title == title).first()


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating

def get_ratings(user_id):
    """Return all ratings for a given user."""
    # user = get_user_by_id(user_id)

    user_ratings = Rating.query.filter(Rating.user_id == user_id).all()

    return user_ratings
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)