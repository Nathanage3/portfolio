one = '''class Match(db.Model):
    __tablename__ = 'matching'
    id = db.Column(db.Integer, primary_key=True)
    finder_id = db.Column(db.Integer, db.ForeignKey('finder.id'), nullable=False)
    lost_id = db.Column(db.Integer, db.ForeignKey('lost.id'), nullable=False)
    matching_percentage = db.Column(db.Float, nullable=False)
    notification_sent = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='matches')
    finder = db.relationship('Finder', back_populates='matches')'''
    
    
two ='''class Match(db.Model):
    __tablename__ = 'matching'
    id = db.Column(db.Integer, primary_key=True)
    finder_id = db.Column(db.Integer, db.ForeignKey('finder.id'), nullable=False)
    lost_id = db.Column(db.Integer, db.ForeignKey('lost.id'), nullable=False)
    matching_percentage = db.Column(db.Float, nullable=False)
    notification_sent = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='matches')
    finder = db.relationship('Finder', back_populates='matches')'''
    
if one == two:
    print("true")
else:
    print("false")
      