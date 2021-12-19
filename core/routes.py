from core import api
from flask import jsonify

ns = api.namespace('/', description = 'Horoscope APIs')

# need to import the routes in the __init__.py file 