from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flask import current_app, flash
from flaskblog import db, login_manager
from flask_login import UserMixin
from flask_mail import Message



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100))
    gender = db.Column(db.String(6), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height_cm = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    birth_city = db.Column(db.String(100), nullable=False)
    skin_color = db.Column(db.String(100), nullable=False)
    primary_school_name = db.Column(db.String(100), nullable=False)
    high_school_name = db.Column(db.String(100))
    university_or_college_name = db.Column(db.String(100))
    current_residence = db.Column(db.String(100))
    email = db.Column(db.String(120), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
   
    matches = db.relationship('Match', backref='user')
    
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
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

'''class Finder(db.Model):
    __tablename__ = 'finder'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100))
    gender = db.Column(db.String(6), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height_cm = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    birth_city = db.Column(db.String(100), nullable=False)
    skin_color = db.Column(db.String(100), nullable=False)
    primary_school_name = db.Column(db.String(100), nullable=False)
    high_school_name = db.Column(db.String(100))
    university_or_college_name = db.Column(db.String(100))
    current_residence = db.Column(db.String(100))
    email = db.Column(db.String(120), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    
    lost_id = db.Column(db.Integer, db.ForeignKey('lost.id'))
    lost = db.relationship('Lost', secondary='finder_lost', back_populates='finders')
    #lost = db.relationship('Lost', back_populates='finder', foreign_keys=[lost_id], uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='finder')
    matches = db.relationship('Match', back_populates='finder')
    
    
    def __repr__(self):
        return f"Finder('{self.first_name}', '{self.middle_name}', '{self.age}', '{self.current_residence}')"



class Lost(db.Model):
    __tablename__ = 'lost'
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
    high_school_name = db.Column(db.String(100))
    university_or_college_name = db.Column(db.String(100))
    relationship_status = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100))
    last_seen = db.Column(db.String(100))
    
    finder_id = db.Column(db.Integer, db.ForeignKey('finder.id'))
    finders = db.relationship('Finder', secondary='finder_lost', back_populates='lost')
    #finder = db.relationship('Finder', back_populates='lost', foreign_keys=[finder_id], uselist=False)
    
    
    
    def __repr__(self):
        return f"Lost('{self.first_name}', '{self.middle_name}', '{self.age}', '{self.relationship_status}')"
    
class FinderLostAssociation(db.Model):
    __tablename__ = 'finder_lost'
    finder_id = db.Column(db.Integer, db.ForeignKey('finder.id'), primary_key=True)
    lost_id = db.Column(db.Integer, db.ForeignKey('lost.id'), primary_key=True)
'''    
class SearchForm:
    def __init__(self, gender, skin_color,birth_city, age, height_cm,
                 first_name, middle_name, last_name, nationality):
        self.gender = gender
        self.skin_color = skin_color
        self.birth_city = birth_city
        self.age = age
        self.height_cm = height_cm
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nationality = nationality
        
    def search_people(search_form):
        query = (
            db.session.query(User)
            .filter(User.skin_color)
            .filter(User.birth_city)
            .filter(User.age)
            .filter(User.height_cm)
            .filter(User.first_name)
            .filter(User.middle_name)
            .filter(User.last_name)
            .filter(User.nationality)
        )
    
        results = query.all()
        return results


class Match(db.Model):
    __tablename__ = 'matching'
    id = db.Column(db.Integer, primary_key=True)
    matching_percentage = db.Column(db.Float, nullable=False)
    notification_sent = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    
    def calculate_matching_percentage(self, user):
        # ... existing code ...
        # Calculate the matching percentage
        matching_percentage = (score / 100) * 100

        return matching_percentage
        
        
    @classmethod
    def find_matches(cls, search_form):
        # Use the SearchForm to get potential matches
        potential_matches = SearchForm.search_people(search_form)

        matches = []
        # For each potential match, calculate the matching percentage
        for lost in potential_matches:
            user = User.query.get(search_form.id)
            matching_percentage = cls.calculate_matching_percentage(user)

            # If the matching percentage is above a certain threshold, store the match
            if matching_percentage > 50:
                match = cls(user_id=search_form.id, matching_percentage=matching_percentage)
                db.session.add(match)
                matches.append(match)

        db.session.commit()

        return matching_percentage
    def send_notification_email(self, email, role):
        # Customize the email subject and body based on the role
        subject = f"Match Found: {role}"
        body = f"Congratulations! You have a match as a {role}. Login to your account to view details."

        # Create a Message instance
        message = Message(subject, recipients=[User.email], body=body)

    
