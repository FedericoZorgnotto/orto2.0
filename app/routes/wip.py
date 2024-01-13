from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
wip_bp = Blueprint('wip', __name__)


@wip_bp.route('/')
def index():
    return render_template('wip.html')

