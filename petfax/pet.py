from flask import (Blueprint, render_template, url_for)

import json
pets =json.load(open('./pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html',pets=pets)

