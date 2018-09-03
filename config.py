#added after changing folder structure
import os
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    #added after changing folder structure
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cherucole:cherucole@localhost/watchlist'


class ProdConfig(Config):
    '''
    production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Dev't configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG= True

#added after changing folder structure
config_options = {
'development':DevConfig,
'production':ProdConfig
}