import flask
from flask import flash
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required
from flask_login import current_user
from flask_user import roles_required
from app.models import Date, Attendance
from app.forms import DateForm

# define the blueprint
bp_user = Blueprint('user-view', __name__, template_folder='pages', static_folder='user-static')


# all routes

# index is list view
@bp_user.route('/')
@roles_required('Benutzer')
def home():
    attendances = Attendance.objects(user=current_user)
    return render_template('user_page.html', kurse=attendances, current_user=current_user, info=session)

@bp_user.route('/print', methods=['POST'])
def handle_print():
    flash('Ihre Datei wird gedruckt.', 'success')
    return redirect(url_for('user-view.home'))

@bp_user.route('/print', methods=['POST'])
def handle_done():
    flash('Sie nehmen am Kurs teil.', 'success')
    return redirect(url_for('user-view.home'))
