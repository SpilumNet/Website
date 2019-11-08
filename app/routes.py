import importlib.util
import os
import sys

from flask import render_template

from app import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('essential/404.html'), 404


@app.route('/')
def index():
    project_list = []
    for project in os.listdir('./app/projects'):
        project_list.append(project)
    return render_template('index.html', projects=project_list)


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

for module in os.listdir('./app/modules'):
    spec = importlib.util.spec_from_file_location(module, 'app/modules/{}/{}.py'.format(module, module))
    moduler = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(moduler)
    sys.modules[module] = moduler
    app.register_blueprint(moduler.bp)
