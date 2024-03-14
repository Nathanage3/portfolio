from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


'''class RegistrationForm(FlaskForm):
    
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
'''
class UserFormPage1(FlaskForm):
   
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Next')

# Page 2
class UserFormPage2(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    nickname = StringField('Nickname')
    gender = StringField('Gender', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    
    GENDER_CHOICES = [
        ('select', 'Please Choose'),
        ('female', 'F'),
        ('male', 'M')
        
    ]
    
    gender = SelectField('gender', choices=GENDER_CHOICES)
    
    submit = SubmitField('Next')
class UserFormPage3(FlaskForm):
    height_cm = StringField('Height (cm)', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired()])
    birth_city = StringField('Home town', validators=[DataRequired()])
    skin_color = StringField('Skin Color', validators=[DataRequired(), Length(min=2, max=20)])
    
    COUNTRY_CHOICES = [
    ('select', 'Please Choose'),   
    ('afghanistan', 'Afghanistan'),
    ('albania', 'Albania'),
    ('algeria', 'Algeria'),
    ('andorra', 'Andorra'),
    ('angola', 'Angola'),
    ('antigua_and_barbuda', 'Antigua and Barbuda'),
    ('argentina', 'Argentina'),
    ('armenia', 'Armenia'),
    ('australia', 'Australia'),
    ('austria', 'Austria'),
    ('azerbaijan', 'Azerbaijan'),
    ('bahamas', 'Bahamas'),
    ('bahrain', 'Bahrain'),
    ('bangladesh', 'Bangladesh'),
    ('barbados', 'Barbados'),
    ('belarus', 'Belarus'),
    ('belgium', 'Belgium'),
    ('belize', 'Belize'),
    ('benin', 'Benin'),
    ('bhutan', 'Bhutan'),
    ('bolivia', 'Bolivia'),
    ('bosnia_and_herzegovina', 'Bosnia and Herzegovina'),
    ('botswana', 'Botswana'),
    ('brazil', 'Brazil'),
    ('brunei', 'Brunei'),
    ('bulgaria', 'Bulgaria'),
    ('burkina_faso', 'Burkina Faso'),
    ('burundi', 'Burundi'),
    ('cabo_verde', 'Cabo Verde'),
    ('cambodia', 'Cambodia'),
    ('cameroon', 'Cameroon'),
    ('canada', 'Canada'),
    ('central_african_republic', 'Central African Republic'),
    ('chad', 'Chad'),
    ('chile', 'Chile'),
    ('china', 'China'),
    ('colombia', 'Colombia'),
    ('comoros', 'Comoros'),
    ('congo', 'Congo'),
    ('costa_rica', 'Costa Rica'),
    ('croatia', 'Croatia'),
    ('cuba', 'Cuba'),
    ('cyprus', 'Cyprus'),
    ('czech_republic', 'Czech Republic'),
    ('denmark', 'Denmark'),
    ('djibouti', 'Djibouti'),
    ('dominica', 'Dominica'),
    ('dominican_republic', 'Dominican Republic'),
    ('east_timor', 'East Timor'),
    ('ecuador', 'Ecuador'),
    ('egypt', 'Egypt'),
    ('el_salvador', 'El Salvador'),
    ('equatorial_guinea', 'Equatorial Guinea'),
    ('eritrea', 'Eritrea'),
    ('estonia', 'Estonia'),
    ('eswatini', 'Eswatini'),
    ('ethiopia', 'Ethiopia'),
    ('fiji', 'Fiji'),
    ('finland', 'Finland'),
    ('france', 'France'),
    ('gabon', 'Gabon'),
    ('gambia', 'Gambia'),
    ('georgia', 'Georgia'),
    ('germany', 'Germany'),
    ('ghana', 'Ghana'),
    ('greece', 'Greece'),
    ('grenada', 'Grenada'),
    ('guatemala', 'Guatemala'),
    ('guinea', 'Guinea'),
    ('guinea_bissau', 'Guinea-Bissau'),
    ('guyana', 'Guyana'),
    ('haiti', 'Haiti'),
    ('honduras', 'Honduras'),
    ('hungary', 'Hungary'),
    ('iceland', 'Iceland'),
    ('india', 'India'),
    ('indonesia', 'Indonesia'),
    ('iran', 'Iran'),
    ('iraq', 'Iraq'),
    ('ireland', 'Ireland'),
    ('israel', 'Israel'),
    ('italy', 'Italy'),
    ('ivory_coast', 'Ivory Coast'),
    ('jamaica', 'Jamaica'),
    ('japan', 'Japan'),
    ('jordan', 'Jordan'),
    ('kazakhstan', 'Kazakhstan'),
    ('kenya', 'Kenya'),
    ('kiribati', 'Kiribati'),
    ('korea_north', 'Korea, North'),
    ('korea_south', 'Korea, South'),
    ('kosovo', 'Kosovo'),
    ('kuwait', 'Kuwait'),
    ('kyrgyzstan', 'Kyrgyzstan'),
    ('laos', 'Laos'),
    ('latvia', 'Latvia'),
    ('lebanon', 'Lebanon'),
    ('lesotho', 'Lesotho'),
    ('liberia', 'Liberia'),
    ('libya', 'Libya'),
    ('liechtenstein', 'Liechtenstein'),
    ('lithuania', 'Lithuania'),
    ('luxembourg', 'Luxembourg'),
    ('madagascar', 'Madagascar'),
    ('malawi', 'Malawi'),
    ('malaysia', 'Malaysia'),
    ('maldives', 'Maldives'),
    ('mali', 'Mali'),
    ('malta', 'Malta'),
    ('marshall_islands', 'Marshall Islands'),
    ('mauritania', 'Mauritania'),
    ('mauritius', 'Mauritius'),
    ('mexico', 'Mexico'),
    ('micronesia', 'Micronesia'),
    ('moldova', 'Moldova'),
    ('monaco', 'Monaco'),
    ('mongolia', 'Mongolia'),
    ('montenegro', 'Montenegro'),
    ('morocco', 'Morocco'),
    ('mozambique', 'Mozambique'),
    ('myanmar', 'Myanmar'),
    ('namibia', 'Namibia'),
    ('nauru', 'Nauru'),
    ('nepal', 'Nepal'),
    ('netherlands', 'Netherlands'),
    ('new_zealand', 'New Zealand'),
    ('nicaragua', 'Nicaragua'),
    ('niger', 'Niger'),
    ('nigeria', 'Nigeria'),
    ('north_macedonia', 'North Macedonia'),
    ('norway', 'Norway'),
    ('oman', 'Oman'),
    ('pakistan', 'Pakistan'),
    ('palau', 'Palau'),
    ('panama', 'Panama'),
    ('papua_new_guinea', 'Papua New Guinea'),
    ('paraguay', 'Paraguay'),
    ('peru', 'Peru'),
    ('philippines', 'Philippines'),
    ('poland', 'Poland'),
    ('portugal', 'Portugal'),
    ('qatar', 'Qatar'),
    ('romania', 'Romania'),
    ('russia', 'Russia'),
    ('rwanda', 'Rwanda'),
    ('saint_kitts_and_nevis', 'Saint Kitts and Nevis'),
    ('saint_lucia', 'Saint Lucia'),
    ('saint_vincent_and_the_grenadines', 'Saint Vincent and the Grenadines'),
    ('samoa', 'Samoa'),
    ('san_marino', 'San Marino'),
    ('sao_tome_and_principe', 'Sao Tome and Principe'),
    ('saudi_arabia', 'Saudi Arabia'),
    ('senegal', 'Senegal'),
    ('serbia', 'Serbia'),
    ('seychelles', 'Seychelles'),
    ('sierra_leone', 'Sierra Leone'),
    ('singapore', 'Singapore'),
    ('slovakia', 'Slovakia'),
    ('slovenia', 'Slovenia'),
    ('solomon_islands', 'Solomon Islands'),
    ('somalia', 'Somalia'),
    ('south_africa', 'South Africa'),
    ('south_sudan', 'South Sudan'),
    ('spain', 'Spain'),
    ('sri_lanka', 'Sri Lanka'),
    ('sudan', 'Sudan'),
    ('suriname', 'Suriname'),
    ('sweden', 'Sweden'),
    ('switzerland', 'Switzerland'),
    ('syria', 'Syria'),
    ('taiwan', 'Taiwan'),
    ('tajikistan', 'Tajikistan'),
    ('tanzania', 'Tanzania'),
    ('thailand', 'Thailand'),
    ('togo', 'Togo'),
    ('tonga', 'Tonga'),
    ('trinidad_and_tobago', 'Trinidad and Tobago'),
    ('tunisia', 'Tunisia'),
    ('turkey', 'Turkey'),
    ('turkmenistan', 'Turkmenistan'),
    ('tuvalu', 'Tuvalu'),
    ('uganda', 'Uganda'),
    ('ukraine', 'Ukraine'),
    ('united_arab_emirates', 'United Arab Emirates'),
    ('united_kingdom', 'United Kingdom'),
    ('united_states', 'United States'),
    ('uruguay', 'Uruguay'),
    ('uzbekistan', 'Uzbekistan'),
    ('vanuatu', 'Vanuatu'),
    ('vatican_city', 'Vatican City'),
    ('venezuela', 'Venezuela'),
    ('vietnam', 'Vietnam'),
    ('yemen', 'Yemen'),
    ('zambia', 'Zambia'),
    ('zimbabwe', 'Zimbabwe')]
    nationality = SelectField('nationality', choices=COUNTRY_CHOICES)
    
    SKIN_TONE_CHOICES = [
        ('select', 'Please Choose'),
        ('very fair', 'Very fair'),
        ('light', 'Fair'),
        ('medium', 'Medium'),
        ('rich_brown', 'Brown'),
        ('olive', 'Olive'),
        ('black', 'Black')
        ]
    skin_color = SelectField('Skin Color', choices=SKIN_TONE_CHOICES)
    submit = SubmitField('Next')
    
class UserFormPage4(FlaskForm):
    primary_school_name = StringField('Primary School Name', validators=[DataRequired(), Length(min=2, max=20)])
    high_school_name = StringField('High School Name')
    university_or_college_name = StringField('University or College')
    current_residence = StringField('Current Residence', validators=[DataRequired(), Length(min=2, max=20)])
    occupation = StringField('Occupation', validators=[DataRequired()])
    
    OCCUPATION_CHOICES = [
    ('select', 'Please Choose'),
    ('accountant', 'Accountant'),
    ('actor', 'Actor'),
    ('air_traffic_controller', 'Air Traffic Controller'),
    ('archaeologist', 'Archaeologist'),
    ('architect', 'Architect'),
    ('artist', 'Artist'),
    ('astronaut', 'Astronaut'),
    ('athlete', 'Athlete'),
    ('bank_manager', 'Bank Manager'),
    ('barista', 'Barista'),
    ('broker', 'Broker'),
    ('chef', 'Chef'),
    ('clerk', 'Clerk'),
    ('consultant', 'Consultant'),
    ('court_reporter', 'Court Reporter'),
    ('data_scientist', 'Data Scientist'),
    ('dentist', 'Dentist'),
    ('designer', 'Designer'),
    ('doctor', 'Doctor'),
    ('electrician', 'Electrician'),
    ('engineer', 'Engineer'),
    ('entrepreneur', 'Entrepreneur'),
    ('event_planner', 'Event Planner'),
    ('farmer', 'Farmer'),
    ('fashion_designer', 'Fashion Designer'),
    ('firefighter', 'Firefighter'),
    ('frontend', 'Frontend Developer'),
    ('gardener', 'Gardener'),
    ('geologist', 'Geologist'),
    ('guard', 'Guard'),
    ('hairdresser', 'Hairdresser'),
    ('journalist', 'Journalist'),
    ('landscaper', 'Landscaper'),
    ('lawyer', 'Lawyer'),
    ('lecturer', 'Lecturer'),
    ('librarian', 'Librarian'),
    ('marine_biologist', 'Marine Biologist'),
    ('match', 'Match'),
    ('mechanic', 'Mechanic'),
    ('merchant', 'Merchant'),
    ('musician', 'Musician'),
    ('nurse', 'Nurse'),
    ('paramedic', 'Paramedic'),
    ('paralegal', 'Paralegal'),
    ('pharmacist', 'Pharmacist'),
    ('photographer', 'Photographer'),
    ('pilot', 'Pilot'),
    ('plumber', 'Plumber'),
    ('police_officer', 'Police Officer'),
    ('priest', 'Priest'),
    ('psychologist', 'Psychologist'),
    ('radiologist', 'Radiologist'),
    ('researcher', 'Researcher'),
    ('salesperson', 'Salesperson'),
    ('scientist', 'Scientist'),
    ('social_worker', 'Social Worker'),
    ('software_developer', 'Software Developer'),
    ('tailor', 'Tailor'),
    ('teacher', 'Teacher'),
    ('tour_guide', 'Tour Guide'),
    ('translator', 'Translator'),
    ('truck_driver', 'Truck Driver'),
    ('urban_planner', 'Urban Planner'),
    ('veterinarian', 'Veterinarian'),
    ('veterinary_technician', 'Veterinary Technician'),
    ('waiter/waitress', 'Waiter/Waitress'),
    ('wedding_planner', 'Wedding Planner'),
    ('writer', 'Writer'),
    ('zoologist', 'Zoologist'),
    ('other', 'Other')
]
    
    occupation= SelectField('occupation', choices=OCCUPATION_CHOICES)

    submit = SubmitField('Sign Up')
    
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    nickname = StringField('Nickname')
    gender = StringField('Gender', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    height_cm = StringField('Height (cm)', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired()])
    birth_city = StringField('Home town', validators=[DataRequired()])
    skin_color = StringField('Skin Color', validators=[DataRequired(), Length(min=2, max=20)])
    primary_school_name = StringField('Primary School Name', validators=[DataRequired(), Length(min=2, max=20)])
    high_school_name = StringField('High School Name')
    university_or_college_name = StringField('University or College')
    current_residence = StringField('Current Residence', validators=[DataRequired(), Length(min=2, max=20)])
    occupation = StringField('Occupation', validators=[DataRequired()])
    
    
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')