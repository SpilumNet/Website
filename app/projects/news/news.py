import json

from flask import Blueprint, render_template

bp = Blueprint('news', __name__)


def get_news():
    with open('./app/static/projects/news/news.json') as f:
        news_obj = json.loads(f.read())
    return news_obj


@bp.route('/projects/news')
def news():
    object_list = get_news()
    return render_template('projects/news/index.html', object_list=object_list, title="News")


@bp.route('/projects/news/<id>')
def post(id):
    object_list = get_news()
    for object in object_list:
        if object['id'] == id:
            return render_template('projects/news/post.html', object=object)
    abort(404)
