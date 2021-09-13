from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5001/pokemondb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)

class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    name = db.Column(db.String())
    img_url = db.Column(db.String())

    def __init__(self, url, name):
        self.img_url = url
        self.name = name


    def __repr__(self):
        return f'<id {self.id}>'
        
def get_db():
    return db

def create_app():
    app.config['SECRET_KEY'] = 'jenna sleeps on the floor'
    return app


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/insert')
def insertToDB():
    raichu = Pokemon("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png", "Raichu")
    db.session.add(raichu)
    return "Successful"
