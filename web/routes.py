from flask import Blueprint, render_template, redirect, url_for, request
from configs import Name_Project
app = Blueprint('app', __name__, template_folder='templates', url_prefix=f'/{Name_Project}')

@app.route('/')
def index():
    return render_template('home.html')
    # return 'Hellooo'