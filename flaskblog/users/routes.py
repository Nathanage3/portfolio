from flask import (render_template, url_for, flash,
                   redirect, request, session, Blueprint)
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (UserFormPage1, UserFormPage2, UserFormPage3,
                                   UserFormPage4, LoginForm,
                                   UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

"""################################"""
'''@users.route('/page1', methods=['GET', 'POST'])
def form_page1():
    form = UserFormPage1()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('You have successfully finished the first step\nYou are remaining with three steps', 'success')
        return redirect(url_for('users.form_page2'))
    return render_template('form_page1.html', title='Register', form=form)

@users.route('/page2', methods=['GET', 'POST'])
def form_page2():
    form = UserFormPage2()
    if form.validate_on_submit():
        page2 = UserFormPage2(first_name=form.first_name.data,
                              middle_name=form.middle_name.data,
                              last_name=form.last_name.data,
                              nickname=form.nickname.data,
                              gender=form.gender.data,
                              age=form.age.data)
        db.session.add(page2)
        db.session.commit()
        # When you're on the final page, save all the data to the database
        user = User.query.filter_by(username=session['username']).first()
        # Update the user's details
        user.first_name = form.first_name.data
        user.middle_name = form.middle_name.data
        user.last_name = form.last_name.data
        user.nickname = form.nickname.data
        user.gender = form.gender.data
        user.age = form.age.data
        # Commit the changes to the database
        db.session.commit()
        flash('You have successfully finished the second step\nYou are remaining with two more steps', 'success')
        return redirect(url_for('users.form_page3'))
    return render_template('form_page2.html', title='Register', form=form)'''

@users.route('/page1', methods=['GET', 'POST'])
def form_page1():
    form = UserFormPage1()
    if form.validate_on_submit():
        # Store form data in session
        session['username'] = form.username.data
        session['email'] = form.email.data
        session['password'] = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash('You have successfully finished the first step\nYou are remaining with three steps', 'success')
        return redirect(url_for('users.form_page2'))
    return render_template('form_page1.html', title='Register', form=form)

@users.route('/page2', methods=['GET', 'POST'])
def form_page2():
    form = UserFormPage2()
    if form.validate_on_submit():
        # Store form data in session
        session['first_name'] = form.first_name.data
        session['middle_name'] = form.middle_name.data
        session['last_name'] = form.last_name.data
        session['nickname'] = form.nickname.data
        session['gender'] = form.gender.data
        session['age'] = form.age.data
        # Create User object and commit to database
        #user = User(username=session['username'], email=session['email'], password=session['password'],
                    #first_name=session['first_name'], middle_name=session['middle_name'], last_name=session['last_name'],
                    #nickname=session['nickname'], gender=session['gender'], age=session['age'])  # Set a default value
        #db.session.add(user)
        #db.session.commit()
        flash('You have successfully finished the second step\nYou are remaining with two more steps', 'success')
        return redirect(url_for('users.form_page3'))
    return render_template('form_page2.html', title='Register', form=form)

@users.route('/page3', methods=['GET', 'POST'])
def form_page3():
    form = UserFormPage3()
    if form.validate_on_submit():
        # Retrieve the user from the database
        #user = User.query.filter_by(username=session['username']).first()
        # Update the user's details
        session['height_cm'] = form.height_cm.data
        session['skin_color'] = form.skin_color.data
        session['birth_city'] = form.birth_city.data
        session['nationality'] = form.nationality.data
        # Commit the changes to the database
        #db.session.commit()
        flash('You have successfully finished the three steps\nYou are remaining with one step', 'success')
        return redirect(url_for('users.form_page4'))
    return render_template('form_page3.html', title='Register', form=form)

@users.route('/page4', methods=['GET', 'POST'])
def form_page4():
    form = UserFormPage4()
    if form.validate_on_submit():
        # Retrieve the user from the database
        #user = User.query.filter_by(username=session['username']).first()
        # Update the user's details
        session['primary_school_name'] = form.primary_school_name.data
        session['high_school_name'] = form.high_school_name.data
        session['university_or_college_name'] = form.university_or_college_name.data
        session['current_residence'] = form.current_residence.data
        session['occupation'] = form.occupation.data
        # Commit the changes to the database
        user = User(username=session['username'],
                    email=session['email'],
                    password=session['password'],
                    first_name=session['first_name'],
                    middle_name=session['middle_name'],
                    last_name=session['last_name'],
                    nickname=session['nickname'],
                    gender=session['gender'],
                    age=session['age'],
                    height_cm=session['height_cm'],
                    nationality=session['nationality'],
                    birth_city=session['birth_city'],
                    skin_color=session['skin_color'],
                    primary_school_name=session['primary_school_name'],
                    high_school_name=session['high_school_name'],
                    university_or_college_name=session['university_or_college_name'],
                    occupation=session['occupation'],
                    current_residence=session['current_residence'])
        db.session.add(user)
        db.session.commit()
        #db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('form_page4.html', title='Register', form=form)


"""#################################"""

'''@users.route('", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)
'''

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.first_name = form.first_name.data
        current_user.middle_name = form.middle_name.data
        current_user.last_name = form.last_name.data
        current_user.nickname = form.nickname.data
        current_user.gender = form.gender.data
        current_user.age = form.age.data
        current_user.height_cm = form.height_cm.data
        current_user.nationality = form.nationality.data
        current_user.birth_city = form.birth_city.data
        current_user.skin_color = form.skin_color.data
        current_user.primary_school_name = form.primary_school_name.data
        current_user.high_school_name = form.high_school_name.data
        current_user.university_or_college_name = form.university_or_college_name.data
        current_user.current_residence = form.current_residence.data
        current_user.occupation = form.occupation.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        image_file = url_for('static', filename='pics/' + current_user.image_file)
        form.first_name.data = current_user.first_name
        current_user.middle_name = form.middle_name.data
        form.last_name.data = current_user.last_name
        form.nickname.data = current_user.nickname
        form.gender.data = current_user.gender
        form.age.data = current_user.age
        form.height_cm.data = current_user.height_cm
        form.nationality.data = current_user.nationality
        form.birth_city.data = current_user.birth_city
        form.skin_color.data = current_user.skin_color
        form.primary_school_name.data = current_user.primary_school_name
        form.high_school_name.data = current_user.high_school_name
        form.university_or_college_name.data = current_user.university_or_college_name
        form.current_residence.data = current_user.current_residence
        form.occupation.data = current_user.occupation

    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
