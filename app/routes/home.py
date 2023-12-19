from flask import Blueprint, render_template
import datetime
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return render_template('home/home.html', ora=datetime.datetime.now().strftime("%H:%M:%S"))