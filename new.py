from flaskblog import db
from flaskblog.models import User, Finder, Lost  # Adjust the imports based on your project structure

# Example: Inserting values into the User table
new_user = User(username='john_doe', email='john@example.com', password='hashed_password')
db.session.add(new_user)
db.session.commit()

# Example: Inserting values into the Finder table
new_finder = Finder(first_name='Alice', middle_name='M', last_name='Finder', age=25, height_cm=170, nationality='CountryA', current_residence='CityX', email='alice@example.com')
db.session.add(new_finder)
db.session.commit()

# Example: Inserting values into the Lost table
new_lost = Lost(first_name='Bob', middle_name='L', last_name='Lost', age=30, height_cm=180, nationality='CountryB', relationship_status='Single', last_seen='CityY')
db.session.add(new_lost)
db.session.commit()
