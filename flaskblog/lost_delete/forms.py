from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class LostForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    middle_name = StringField('Middle Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name')
    nickname = StringField('Nickname')
    gender = StringField('Gender', validators=[DataRequired(), Length(min=1, max=6)])
    age = IntegerField('Age', validators=[DataRequired()])
    height_cm = IntegerField('Height (cm)', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired(), Length(min=2, max=100)])
    birth_city = StringField('Home Town')
    skin_color = StringField('Skin Color', validators=[DataRequired(), Length(min=2, max=20)])
    primary_school_name = StringField('Primary School Name')
    high_school_name = StringField('High School Name')
    university_or_college_name = StringField('University or College')
    relationship_status = StringField('Relationship Status', validators=[DataRequired(), Length(min=5, max=25)])
    occupation = StringField('Occupation', validators=[DataRequired()])
    last_seen = StringField('Last Seen')
    
    LAST_SEEN_CHOICES = [
        ('1', '3 months ago'),
        ('2', '6 months ago'),
        ('3', '9 months ago'),
        ('4', '1 year ago'),
        ('5', '2 years ago'),
        ('6', '3 years ago'),
        ('7', '4 years ago'),
        ('8', '5 years ago'),
        ('9', '6 years ago'),
        ('10', '8 years ago'),
        ('11', '10 years  ago'),
        ('12', 'more than 10 years ago')
    ]
    
    last_seen = SelectField('last_seen', choices=LAST_SEEN_CHOICES)
    
    GENDER_CHOICES = [
        ('female', 'F'),
        ('male', 'M')
        
    ]
    
    gender = SelectField('gender', choices=GENDER_CHOICES)
    
    SKIN_TONE_CHOICES = [
        ('pale', 'Pale'),
        ('fair', 'Fair'),
        ('medium', 'Medium'),
        ('olive', 'Olive'),
        ('rich_brown', 'Rich Brown'),
        ('white', 'White'),
        ('black', 'Black')
        ]
    skin_color = SelectField('skin_color', choices=SKIN_TONE_CHOICES)
    
    OCCUPATION_CHOICES = [
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
    

    
    RELATIONSHIP_CHOICES = [
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('sister', 'Sister'),
        ('brother', 'Brother'),
        ('uncle', 'Uncle'),
        ('aunt', 'Aunt'),
        ('grandmother', 'Grandmother'),
        ('grandfather', 'Grandfather'),
        ('marriage family', 'Marriage Family'),
        ('normal friend', 'Friend'),
        ('ex-wife', 'Ex-wife'),
        ('ex-husband', 'Ex-husband'),
        ('ex-girlfriend', 'Ex-girlfriend'),
        ('ex-boyfriend', 'Ex-boyfriend'),
        ('son', 'Son'),
        ('daughter', 'Daughter'),
        ('old neighbour', 'Old Neighbour'),
        ('old classmate', 'Old Classmate'),
        ('colleague', 'Colleague'),
        ('other', 'Other')
        
        # ... add more choices as needed ...
    ]

    relationship_status = SelectField('Relationship Status', choices=RELATIONSHIP_CHOICES)
    
    UNIVERSITY_CHOICES = [
        ('Adama Science and Technology University', 'Adama Science and Technology University'),
        ('Addis Ababa Science and Technology University', 'Addis Ababa Science and Technology University'),
        ('Addis Ababa University', 'Addis Ababa University'),
        ('Adigrat University', 'Adigrat University'),
        ('Aksum University', 'Aksum University'),
        ('Ambo University', 'Ambo University'),
        ('Arba Minch University', 'Arba Minch University'),
        ('Assosa University', 'Assosa University'),
        ('Bahir Dar University', 'Bahir Dar University'),
        ('Bule Hora University', 'Bule Hora University'),
        ('Debre Berhan University', 'Debre Berhan University'),
        ('Debre Markos University', 'Debre Markos University'),
        ('Debre Tabor University', 'Debre Tabor University'),
        ('Dilla University', 'Dilla University'),
        ('Dire Dawa University', 'Dire Dawa University'),
        ('Ethiopian Civil Service University', 'Ethiopian Civil Service University'),
        ('Haramaya University', 'Haramaya University'),
        ('Hawassa University', 'Hawassa University'),
        ('Jigjiga University', 'Jigjiga University'),
        ('Jimma University', 'Jimma University'),
        ('Madda Walabu University', 'Madda Walabu University'),
        ('Mattu University', 'Mattu University'),
        ('Mekelle University', 'Mekelle University'),
        ('Mizan Tepi University', 'Mizan Tepi University'),
        ('Oromia State University', 'Oromia State University'),
        ('Rift Valley University', 'Rift Valley University'),
        ('Samara University', 'Samara University'),
        ('Unity University', 'Unity University'),
        ('University of Gondar', 'University of Gondar'),
        ('Wachamo University', 'Wachamo University'),
        ('Wolaita Sodo University', 'Wolaita Sodo University'),
        ('Woldia University', 'Woldia University'),
        ('Wolkite University', 'Wolkite University'),
        ('Wollega University', 'Wollega University'),
        ('Wollo University', 'Wollo University'),
        ('private college', 'Private College'),
        ('public college', 'Public College'),
        ('TVET', 'TVET'),
        ('other', 'Other')
    ]

    university = SelectField('University', choices=UNIVERSITY_CHOICES)
    
    COUNTRY_CHOICES = [
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
    ('zimbabwe', 'Zimbabwe')
]

    
    nationality = SelectField('nationality', choices=COUNTRY_CHOICES)

    
    
    submit = SubmitField('Submit')
