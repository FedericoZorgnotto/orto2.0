from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
wip_bp = Blueprint('products_bp', __name__)


@wip_bp.route('/products_bp')
def products_bp():
    pass
