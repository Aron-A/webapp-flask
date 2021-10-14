# Setando Configurações
# -- Gerais --
Name_Project = 'template'
MODO = 'DEV' #'PROD'

if MODO == 'DEV':
    Port = 8999
else:
    Port = 8000

from web.routes import app as route
from flask import Flask

app = Flask(__name__)
app.register_blueprint(route)
