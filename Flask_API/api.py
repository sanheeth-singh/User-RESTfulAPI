from flask import Flask, render_template, url_for
from resources import Users, User
from flask_restful import Api
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
api = Api(app)

api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')


@app.route("/")
def home():
    return render_template('project_info.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)