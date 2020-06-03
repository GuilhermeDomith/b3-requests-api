from flask import Flask

app = Flask(__name__)

from app.url_converters import RegexConverter
app.url_map.converters['regex'] = RegexConverter

from app import api

