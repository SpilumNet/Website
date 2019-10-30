from flask import Blueprint, render_template

bp = Blueprint('ghac', __name__)


@bp.route('/projects/ghac')
def guilt():
    return render_template('projects/ghac/index.html')
