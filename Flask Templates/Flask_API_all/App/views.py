from flask import *
from flask_cors import CORS
import logging
from configparser import ConfigParser
# from App.utils import *
import App.utils as utils
import App.specific_functions as specific_functions

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
CORS(app)

config = ConfigParser()
config.read('config/config.ini')
FIRSTNAME = config['VARIABLEENV']['FIRSTNAME']
SURNAME = config['VARIABLEENV']['SURNAME']

@app.route('/test', methods=["GET"])
def test():
    return {'message': 'this is a test'}

@app.route('/test2', methods=["GET"])
def test2():
    name = specific_functions.get_full_name()
    return render_template('index.html', text=name)

@app.route('/test3', methods=["GET"])
def test3():
    FIRSTNAME_uppercase = utils.change_uppercase(FIRSTNAME)
    return {'message': FIRSTNAME_uppercase}

