from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    :return:
    '''
    message="Hello World Again Dynamic"
    funnymessage='this is a funny message test'
    return render_template('index.html', message12=message, funny=funnymessage)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    view movie page function that returns the movie details page and its data
    :param movie_id:
    :return:
    '''
    return render_template('movie.html', id=movie_id)

def index():
    '''
    view root page function that returns the index page and its data
    :return:
    '''
    myTitle='Home- Welcome to the best movie review site Online'
    return render_template('index.html', title=myTitle)