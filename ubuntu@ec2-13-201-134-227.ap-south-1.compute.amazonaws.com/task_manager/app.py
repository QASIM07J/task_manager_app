from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from routes import *

def init_db():
    from models import User, Task
    with app.app_context():
        db.create_all()

# Run init_db on startup
init_db()

if __name__ == '__main__':
    app.run(debug=True)