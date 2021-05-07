from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask_migrate import Migrate
from may_blog.models import db as root_db, login_manager

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app)

from may_blog import models