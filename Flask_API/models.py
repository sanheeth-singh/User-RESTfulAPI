from flask_sqlalchemy import SQLAlchemy

# 1. Initialize DB without 'app'
db = SQLAlchemy()

# 2. Define the Model
class UserModel(db.Model):
    __tablename__ = 'users' # Good practice to name tables explicitly
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    email = db.Column(db.String(75), unique=True, nullable=False)

    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"