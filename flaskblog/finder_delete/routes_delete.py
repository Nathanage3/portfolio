from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Finder, User
from flaskblog.finder.forms import FinderForm

finder = Blueprint('finder', __name__)


@finder.route('/finder', methods=['GET', 'POST'])
@login_required
def new_finder():
  form = FinderForm()
  if form.validate_on_submit():
    finders = Finder(
                     first_name=form.first_name.data,
                     middle_name=form.middle_name.data,
                     last_name=form.last_name.data,
                     nickname=form.nickname.data,
                     email=current_user.email,
                     gender=form.gender.data,
                     age=form.age.data,
                     height_cm=form.height_cm.data,
                     birth_city=form.birth_city.data,
                     nationality=form.nationality.data,
                     skin_color=form.skin_color.data,
                     primary_school_name=form.primary_school_name.data,
                     high_school_name=form.high_school_name.data,
                     university_or_college_name=form.university_or_college_name.data,
                     current_residence=form.current_residence.data,
                     occupation=form.occupation.data,
                     user_id=current_user.id
                     )
    db.session.add(finders)
    db.session.commit()
    flash('You have successfull completed your personal information!', 'success')
    return redirect(url_for('lost.new_lost'))
  return render_template('create_finder.html', title="Your Personal information",
                         legend="Your Personal information", form=form)