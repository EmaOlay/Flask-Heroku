#pip install flask flask-cors psycopg2 python-decouple python-dotenv
from flask import Flask
from flask_cors import CORS
from config import config

# Routes
from routes import Mangas

app = Flask(__name__)
CORS(app)

def page_not_found(error):
    return "<h1> Not found</h1>",404

if __name__=='__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Mangas.main,url_prefix='/api/mangas')

    # Error handlers
    app.register_error_handler(404,page_not_found)
    app.run()
