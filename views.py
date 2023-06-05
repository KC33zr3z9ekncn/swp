import flask
from flask import flash
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required
from flask_login import current_user
from flask_user import roles_required
from app.models import Date, Attendance, Module
from app.forms import DateForm

# define the blueprint
bp_user = Blueprint('user-view', __name__, template_folder='pages', static_folder='user-static')


# all routes

# index is list view
@bp_user.route('/')
@roles_required('Benutzer')
def home():
    attendances = Attendance.objects(user=current_user)
    available_courses = Date.objects.all()
    for course in available_courses:
        course.participants = Attendance.objects(class_ref=course).count()
    return render_template('user_page.html', kurse=attendances, available_courses=available_courses, current_user=current_user, info=session)

@bp_user.route('/print', methods=['POST'])
def handle_print():
    flash('Ihre Datei wird gedruckt.', 'success')
    return redirect(url_for('user-view.home'))

@bp_user.route('/done', methods=['POST'])
def handle_done():
    flash('Sie nehmen am Kurs teil.', 'success')
    return redirect(url_for('user-view.home'))

@bp_user.route('/close', methods=['POST'])
def handle_close():
    flash('Sie haben den Kurs verlassen.', 'success')
    return redirect(url_for('user-view.home'))
