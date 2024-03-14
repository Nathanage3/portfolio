from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import SearchForm
from flaskblog.finder_form.forms import SearchForm


search = Blueprint('search', __name__)

@search.route('/searchform', methods=['GET', 'POST'])
def searchform():
  form = SearchForm()
  if form.validate_on_submit():
    searches = SearchForm(
                     first_name=form.first_name.data,
                     middle_name=form.middle_name.data,
                     last_name=form.last_name.data,
                     gender=form.gender.data,
                     age=form.age.data,
                     height_cm=form.height_cm.data,
                     birth_city=form.birth_city.data,
                     nationality=form.nationality.data,
                     skin_color=form.skin_color.data
    )
    db.session.add(searches)
    db.session.commit()
    flash("You have successfully submitted", 'success')
    return redirect(url_for('match.result'))
  return render_template('searchform.html', title='Your Finding Result', legend='Your Finding Result', form=form)
    