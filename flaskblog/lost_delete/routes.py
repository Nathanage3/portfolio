from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Lost
from flaskblog.lost.forms import LostForm

lost = Blueprint('lost', __name__)

@lost.route('/lost', methods=['GET', 'POST'])
@login_required
def new_lost():
  form = LostForm()
  if form.validate_on_submit():
    losts = Lost(
    first_name=form.first_name.data,
    middle_name=form.middle_name.data,
    last_name=form.last_name.data,
    nickname=form.nickname.data,
    gender=form.gender.data,
    age=form.age.data,
    height_cm=form.height_cm.data,
    birth_city=form.birth_city.data,
    nationality=form.nationality.data,
    skin_color=form.skin_color.data,
    primary_school_name=form.primary_school_name.data,
    high_school_name=form.high_school_name.data,
    university_or_college_name=form.university_or_college_name.data,
    relationship_status=form.relationship_status.data,
    occupation=form.occupation.data,
    last_seen=form.last_seen.data,
    finder_id=current_user.finder.id)
    
    db.session.add(losts)
    db.session.commit()
    flash("You have successfull completed the lost person's profile!", 'success')
    return redirect(url_for('main.home'))
  return render_template('create_lost.html', title="Lost Person Information",
                         legend="Lost Person Information", form=form)
