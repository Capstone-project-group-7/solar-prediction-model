from flask import Flask
from waitress import serve
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

app = Flask(__name__)


if __name__ == "__main__":
    serve(app)