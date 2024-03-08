from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    nickname = db.Column(db.String(100))
    gender = db.Column(db.String(6), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height_cm = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    birth_city = db.Column(db.String(100))
    skin_color = db.Column(db.String(100), nullable=False)
    primary_school_name = db.Column(db.String(100))
    secondary_school_name = db.Column(db.String(100))
    preparatory_school_name = db.Column(db.String(100))
    university_or_college_name = db.Column(db.String(100))
    

class Lost(BaseModel, db.Model):
    relationship_status = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100))
    last_seen = db.Column(db.String(100))
    finder_id = db.Column(db.Integer, db.ForeignKey('finder.id'))

    def __repr__(self):
        return f"Lost('{self.first_name}', '{self.middle_name}', '{self.age}', '{self.relationship_status}')"


class Finder(BaseModel, db.Model):
    current_residence = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lost_id = db.Column(db.Integer, db.ForeignKey('lost.id'))

    def __repr__(self):
        return f"Finder('{self.first_name}', '{self.middle_name}', '{self.age}', '{self.current_residence}')"

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    finder_id = db.Column(db.Integer, db.ForeignKey('finder.id'), nullable=False)
    lost_id = db.Column(db.Integer, db.ForeignKey('lost.id'), nullable=False)
    matching_percentage = db.Column(db.Float, nullable=False)
    notification_sent = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Match('{self.finder_id}', '{self.lost_id}', '{self.matching_percentage}')"