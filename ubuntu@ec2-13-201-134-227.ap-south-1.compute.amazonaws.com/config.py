import os

class Config:
    # Secret key for Flask sessions
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_dev_secret_key')

    # PostgreSQL database URL from environment variables
    DB_USER = os.environ.get('DB_USER', 'taskuser')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'taskpass')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_NAME = os.environ.get('DB_NAME', 'taskdb')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # (Optional) For loading static files externally
    STATIC_URL = os.environ.get('STATIC_URL', '/static/')
