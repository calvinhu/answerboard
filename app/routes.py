from flask import render_template, flash, redirect, url_for, request, render_template_string
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from flask_babelex import Babel
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

# The Home page is accessible to anyone
@app.route('/')
def home_page():
    return render_template('index.html', title='Home')

# The Members page is only accessible to authenticated users
@app.route('/members')
@login_required    # Use of @login_required decorator
def member_page():
    return render_template('members.html', title='Members')

# The Admin page requires an 'Admin' role.
@app.route('/admin')
@roles_required('Admin')    # Use of @roles_required decorator
def admin_page():
    return render_template('admin.html', title='Admin')
