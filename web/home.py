from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from db.mongo import Database

bp = Blueprint('home', __name__, url_prefix='')


@bp.route('/')
def home():
    database = Database().get_db()
    data_list = list()
    if database["status"] == 200:
        data = database["database"].get_collection('inventory').find({}, {"_id": 0})
        for i in data:
            data_list.append(i)
    else:
        data_list = ""
    return render_template("index.html")
