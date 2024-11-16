from configparser import ConfigParser

config = ConfigParser()
config.read('config/config.ini')
FIRSTNAME = config['VARIABLEENV']['FIRSTNAME']
SURNAME = config['VARIABLEENV']['SURNAME']

def get_full_name():
    return FIRSTNAME + SURNAME
