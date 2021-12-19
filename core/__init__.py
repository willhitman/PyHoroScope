from ensurepip import version
from pydoc import doc
from sys import prefix
from turtle import title
from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version = '1.0',
    title = 'Horoscope API',
    description = 'Get horoscope data easily',
    license = 'MIT',
    contact ='Gift Ruwende',
    contact_url = '#',
    contact_email = 'giftwt9wt@gmail.com',
    doc = '/',
    prefix ='/api/v1'
)


from core import routes
# imported the routes