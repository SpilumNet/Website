from flask import Blueprint, render_template

from . import model

bp = Blueprint('petrol', __name__)


@bp.route('/projects/petrol')
def index():
    obj = model.get_data()
    companies = {}
    for i in obj:
        if i['company'] not in companies:
            companies[i['company']] = {'bensin95': i['bensin95'], 'diesel': i['diesel']}

    while obj:
        minBensin = min(obj, key=lambda x: x['bensin95'])
        if minBensin['bensin95'] < companies[minBensin['company']]['bensin95']:
            companies[minBensin['company']]['bensin95'] = minBensin['bensin95']
        if minBensin['diesel'] < companies[minBensin['company']]['diesel']:
            companies[minBensin['company']]['diesel'] = minBensin['diesel']
        obj.remove(minBensin)

    print(companies)

    return render_template('projects/petrol/index.html', company_list=companies, title='Petrol')
