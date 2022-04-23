"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """This is the homepage."""
    
    return render_template("homepage.html")

@app.route('/movies')
def movies():
    """Shows all the movies."""
    movies = crud.return_all_movies()
    return render_template("all_movies.html", movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """"Show dteails on a particular movie."""
    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)

@app.route('/users')
def display_users():
    users = crud.return_all_users()

    return render_template("users.html", users=users)

@app.route('/users', methods=["POST"])
def account_reg():
    new_user_email = request.form['email']
    new_user_password = request.form['password']

    if crud.get_user_by_email(new_user_email):
        msg = "This account already exists, please log in"
    else:
        new_user = crud.create_user(new_user_email, new_user_password)

        db.session.add(new_user)
        db.session.commit()
        msg = "Your account was successfully created!"
    flash(msg)
    return redirect('/')

@app.route('/users/<user_id>')
def show_user(user_id):
    """"Show dteails on a particular user."""
    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user, user_id=user_id)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", port="5001", debug=True)
