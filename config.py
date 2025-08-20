import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this-secret-key-for-development'

    database_url = os.environ.get('DATABASE_URL')

    if database_url:
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Local fallback for dev
        username = os.environ.get('DB_USER', 'postgres')
        password = os.environ.get('DB_PASS', 'password123')
        server = os.environ.get('DB_SERVER', 'localhost')
        database = os.environ.get('DB_NAME', 'mydb')

        password_encoded = quote_plus(password)
        SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{username}:{password_encoded}@{server}:5432/{database}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
