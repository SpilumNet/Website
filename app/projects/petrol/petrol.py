from flask import Blueprint, render_template

from app.projects.petrol import model

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

    mincompany = min((int(x['bensin95']), int(x['diesel'])) for x in companies.values())
    mincompany = [x for x in companies if (int(companies[x]['bensin95']), int(companies[x]['diesel'])) == mincompany]

    return render_template('projects/petrol/index.html', company_list=companies, title='Petrol', mincompany=mincompany)


@bp.route('/projects/petrol/<id>')
def company(id):
    obj = model.get_data()
    companies = {}
    comp = {}

    for i in obj:
        if i['company'] not in companies:
            companies[i['company']] = {'bensin95': i['bensin95'], 'diesel': i['diesel'], 'locations': []}

    while obj:
        minBensin = min(obj, key=lambda x: x['bensin95'])
        if minBensin['bensin95'] < companies[minBensin['company']]['bensin95']:
            companies[minBensin['company']]['bensin95'] = minBensin['bensin95']
        if minBensin['diesel'] < companies[minBensin['company']]['diesel']:
            companies[minBensin['company']]['diesel'] = minBensin['diesel']
        companies[minBensin['company']]['locations'].append(minBensin['name'])
        obj.remove(minBensin)

    for obj, value in companies.items():
        if str(obj) == id:
            comp[obj] = companies[obj]
            return render_template('projects/petrol/company.html', company=comp)
