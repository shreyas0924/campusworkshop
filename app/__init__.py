"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cha8qn67avj5o481o12g-a.oregon-postgres.render.com",
        database="todo_f73j",
        user="todo_f73j_user",
        password="wr6H1Jl3Gia9ZAPF0WY5K4bM3MKivhgJ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
