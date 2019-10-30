import importlib.util
import os
import sys
from datetime import datetime

from flask import render_template

from app import app


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('essential/404.html'), 404


@app.route('/')
def index():
    project_list = []
    for project in os.listdir('./app/projects'):
        project_list.append(project)
    return render_template('index.html', projects=project_list, now=datetime.utcnow())


@app.route('/about')
def about():
    return render_template('information/about.html')


@app.route('/todo')
def todo():
    return render_template('information/todo.html')


@app.route('/contact')
def contact():
    return render_template('information/contact.html')


for project in os.listdir('./app/projects'):
    spec = importlib.util.spec_from_file_location(project, 'app/projects/{}/{}.py'.format(project, project))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[project] = module
    app.register_blueprint(module.bp)
