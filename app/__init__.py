import os
import sqlalchemy as sql
import json
from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(24)


class Database(object):
    with open("config.json") as f:
        conf = json.load(f)
        engine = sql.create_engine(conf['sql']['uri'])

    def __init__(self):
        self.con = self.engine.connect()
        print("DB initialized")


db = Database()

if not db.con.dialect.has_table(db.con, 'users'):
    db.con.execute('CREATE TABLE IF NOT EXISTS users ('
                   'id SERIAL PRIMARY KEY, '
                   'username VARCHAR(32) NOT NULL, '
                   'passwd VARCHAR(64) NOT NULL, '
                   'email VARCHAR(64) NOT NULL)')
db.con.execute("INSERT INTO users(username, passwd, email)"
               "SELECT 'test', 'test', 'test@test.test'"
               "WHERE NOT EXISTS ("
               "SELECT * FROM users WHERE id=1)")

from app import routes
