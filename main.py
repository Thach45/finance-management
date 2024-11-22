from dotenv import load_dotenv
from flask import render_template
import os
from flask_pymongo import PyMongo
from flask import Flask
from app.Dashboard import home_bp
load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

app.register_blueprint(home_bp)
if __name__ == '__main__':
    app.run(debug=True, port=8000)