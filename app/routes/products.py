from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify

products_bp = Blueprint('products', __name__)


@products_bp.route('/')
def index():
    return "gaga"
