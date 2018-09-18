import os
import logging

from logging import Formatter, FileHandler
from flask import Flask, render_template, request


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    return render_template('index.html')


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


# Default port 8080:
if __name__ == '__main__':
    app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))
