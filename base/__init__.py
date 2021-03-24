import warnings

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'shdbfhrudcjajvhsgdfh'

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/login_with_face'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

database = SQLAlchemy(app)

import base.com.controller
