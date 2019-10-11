from flask import (Blueprint, flash, render_template, request)

bp = Blueprint('kennitala', __name__)


@bp.route('/projects/kennitala', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        kt = request.form['kennitala']
        summa = sum([int(i) for i in str(kt)])
        flash('Útkoman er: ' + str(summa))
    return render_template('projects/kennitala/index.html')
