import os
import pymysql
import json
from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(24)


class Database(object):
    def __init__(self):
        with open("config.json") as f:
            conf = json.load(f)
        host = conf['sql']['host']
        user = conf['sql']['user']
        password = conf['sql']['password']
        db = conf['sql']['db']
        port = conf['sql']['port']

        self.con = pymysql.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            db=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.con.cursor()


db = Database()
db.cur.execute('CREATE TABLE IF NOT EXISTS users ('
               'id INT AUTO_INCREMENT PRIMARY KEY, '
               'user VARCHAR(32) NOT NULL, '
               'pass VARCHAR(64) NOT NULL, '
               'email VARCHAR(64) NOT NULL)')

from app import routes
